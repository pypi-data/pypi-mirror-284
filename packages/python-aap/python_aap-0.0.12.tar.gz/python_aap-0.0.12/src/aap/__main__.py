import argparse
import json
import os
import time
import urllib3

from . import JobTemplate, API, Organization


def build_parser():
    parser = argparse.ArgumentParser(
        description="Trigger jobs and workflows from terminal",
    )

    # More will be added later
    subparsers = parser.add_subparsers(title="subcommands", help="commands help", dest="subcommand", required=True)
    job_parser = subparsers.add_parser("job", help="job help")
    grep_parser = subparsers.add_parser("grep", help="grep help")

    # common arguments
    parser.add_argument('--insecure', dest="insecure", action="store_true",
                        default=False, help="Dont verify ssl certificate")
    parser.add_argument('-p', '--password', dest="password", action="store", default=os.environ.get(
                        "AAP_PASSWORD"), help="Password used for authentication to AAP API (env: AAP_PASSWORD)")
    parser.add_argument('-u', '--username', dest="username", action="store", default=os.environ.get(
                        "AAP_USERNAME"), help="Username used for authentication to AAP API (env: AAP_USERNAME)")
    parser.add_argument('-r', '--retries', dest="retries", action="store",
                        type=int, default=3, help="Number of retries on API error")
    parser.add_argument('-s', '--url', dest="url", action="store",
                        default=os.environ.get('AAP_URL'), help="URL of AAP instance (env: AAP_URL)")

    # Job argument
    job_parser.add_argument("action", choices=["run-job"])

    job_parser.add_argument('-i', '--id', dest="id", action="store",
                            required=True, help="ID of job to run")
    job_parser.add_argument('-f', '--follow', action="store_true", default=False,
                            help="Wait for job to finish execution and report its status")
    job_parser.add_argument('-l', '--limit', dest="limit", action="store",
                            default=[], help="Limit as comma separated list")
    job_parser.add_argument('-j', '--tags', dest="tags", action="store",
                            default=[], help="Job tags as comma separated list")
    job_parser.add_argument('-e', '--extra-vars', dest="extra", action="store",
                            default={}, help="json formatted extra variables")
    job_parser.add_argument('-t', '--poll-timeout', dest="timeout", action="store",
                            type=int, default=5, help="Number of seconds between 2 polling requests to aap")
    job_parser.add_argument('--ignore-fail', dest="ingore_fail", action="store_true",
                            default=False, help="Program will return successfull even if job fails")

    # config grepper
    grep_parser.add_argument("-s", "--search", help="Look for string $string in configuration",
                             dest="needle", action="store", required=True)
    grep_parser.add_argument("-o", "--orgid", help="ID or Name of organization to look for $string in configurations",
                             dest="orgid", action="store", default=None)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # Common parsing logic
    if not args.username or not args.password or not args.url:
        print("Please provide AAP URL and credentials,"
              "either using command line arguments or by setting environment variables.")
        parser.print_help()
        exit(1)

    if args.insecure:
        urllib3.disable_warnings()

    aap = API(args.url, args.username, args.password,
              ssl_verify=not args.insecure, retries=args.retries)

    # TODO: use constants
    if args.subcommand == "job":
        # Jobs parsing logic
        if args.limit:
            args.limit = args.limit.split(',')
        if args.tags:
            args.tags = args.tags.split(',')
        if args.extra:
            try:
                args.extra = json.loads(args.extra)
            except ValueError:
                print(f"Invalid extra variables provided: {args.extra}")
                exit(1)

        print(f"Searching job {args.id}")
        template = JobTemplate.load(args.id, aap)
        if not template:
            print("Job not found")
            exit(1)
        print(f"Job: {template.name}")
        print(f"\tlimit: {args.limit}")
        print(f"\textra variables: {args.extra}")
        print(f"\tjob tags: {args.tags}")
        job = template.launch(args.extra, args.limit, args.tags)
        print(f"\tjob url: {job.url}")

        if not args.follow:
            exit(0)

        print('-' * 40)
        state = job.status
        print(f"Job is {state}")

        while not job.is_running and not job.is_finished:
            time.sleep(args.timeout)
            job._reload()
            if job.status != state:
                state = job.status
                print(f"Job is {state}")
        try:
            last_line = 0
            while job.is_running:
                stdout = job.stdout.splitlines()
                if len(stdout) > last_line:
                    print("\n".join(stdout[last_line:]))
                    last_line = len(stdout)
                time.sleep(args.timeout)
                job._reload()

            stdout = job.stdout.splitlines()
            if len(stdout) > last_line:
                print("\n".join(stdout[last_line:]))
                last_line = len(stdout)
        except Exception:
            print("Error happend during fetching of output")
            state = job.status
            print(f"Job is {state}")
            while job.is_running:
                time.sleep(args.timeout)
                job._reload()
                if job.status != state:
                    state = job.status
                    print(f"Job is {state}")

        exit(not (job.is_successfull or args.ingore_fail))

    elif args.subcommand == "grep":
        def grep_organization(org, needle):
            for project in org.projects:
                if needle in project._data.get('scm_url'):
                    print("/{}/{}/ SCM URL:\n  > {}\n".format(org.name, project.name, project._data.get('scm_url')))

            for template in org.job_templates:
                if needle in template.extra_vars:
                    print("/{}/{}/ Extra variables:\n  > "
                          .format(org.name, template.name)
                          .join([var for var in template.extra_vars.splitlines() if args.needle in var])
                          .join("\n"))

            # Perhaps add credentials into the mix as well
            # for credential in org.credentials:

        # If numeric id is provided:
        if args.orgid is not None and args.orgid.isdigit():
            grep_organization(Organization.load(args.orgid), args.needle)
        # If name is provided or nothing at all
        else:
            for org in Organization.find("" if args.orgid is None else str(args.orgid)):
                grep_organization(org, args.needle)

    else:
        exit(1)


if __name__ == "__main__":
    main()
