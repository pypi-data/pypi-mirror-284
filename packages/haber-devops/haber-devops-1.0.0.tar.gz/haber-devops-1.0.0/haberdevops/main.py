import sys
from haberdevops.config import initialize_config, add_aws_account, list_instances, list_s3_buckets
from haberdevops.ec2 import start_ec2_instance, stop_ec2_instance
from haberdevops.ecr import list_ecr_repositories, create_ecr_repository, delete_ecr_repository, describe_ecr_repository, get_ecr_repository_uri
from haberdevops.s3 import list_s3_buckets, create_s3_bucket, delete_s3_bucket
from haberdevops.ssh import ssh_ec2_instance
from haberdevops.rds import start_rds_instance, stop_rds_instance, list_rds_instances
from haberdevops.tags import list_resources_by_tag
from haberdevops.deploy import  deploy_existing, deploy_new, deploy_cli  
from haberdevops.docker import docker_ls, docker_ps, docker_stop, docker_sh, docker_run
from haberdevops.config import load_config, save_config 
from haberdevops.deploy import get_aws_clients
from haberdevops.route53 import list_records, create_record, delete_record

def main():
    if len(sys.argv) < 2:
        print("Usage: haber-devops <command> [options]")
        return
    command = sys.argv[1]
    if command == 'initialize':
        initialize_config()
    elif command == 'add-account':
        add_account_cli()
    elif command == 'list-instances':
        list_instances_cli()
    elif command == 'ec2':
        ec2_cli()
    elif command == 'ecr-ls':
        list_ecr_cli()
    elif command == 'ecr-create':
        create_ecr_cli()
    elif command == 'ecr-delete':
        delete_ecr_cli()
    elif command == 'ecr-describe':
        describe_ecr_cli()
    elif command == 'ecr-uri':
        ecr_uri_cli()
    elif command == 's3-ls':
        list_s3_cli()
    elif command == 's3-create':
        create_s3_cli()
    elif command == 's3-delete':
        delete_s3_cli()
    elif command == 'ec2-ssh':
        ec2_ssh_cli()
    elif command == 'rds':
        rds_cli()
    elif command == 'rds-ls':
        list_rds_cli()
    elif command == 'deploy':
        deploy_lambda_cli() 
    elif command == 'docker':
        docker_cli()
    elif command == 'route53':
        route53_cli()
    else:
        tag_cli(command)


def add_account_cli():
    profile_name = input("Enter profile name: ")
    access_key = input("Enter AWS Access Key: ")
    secret_key = input("Enter AWS Secret Key: ")
    region = input("Enter AWS Region: ")
    add_aws_account(profile_name, access_key, secret_key, region)

def list_instances_cli():
    profile_name = input("Enter profile name: ")
    list_instances(profile_name)

def ec2_cli():
    if len(sys.argv) < 4:
        print("Usage: haber-devops ec2 <start/stop/ssh> <instance_name> [command]")
        return
    subcommand = sys.argv[2]
    instance_name = sys.argv[3]
    profile_name = input("Enter profile name: ")  # Prompt for profile name
    if subcommand == 'start':
        start_ec2_instance(profile_name, instance_name)
    elif subcommand == 'stop':
        stop_ec2_instance(profile_name, instance_name)
    elif subcommand == 'ssh':
        if len(sys.argv) < 5:
            print("Usage: haber-devops ec2 ssh <instance_name> <command>")
            return
        ssh_command = sys.argv[4]
        ssh_ec2_instance(profile_name, instance_name, ssh_command)
    else:
        print(f"Unknown subcommand: {subcommand}")

def list_ecr_cli():
    profile_name = input("Enter profile name: ")
    repositories = list_ecr_repositories(profile_name)
    if repositories:
        print("ECR Repositories:")
        for repo in repositories:
            print(repo['RepositoryName'])
    else:
        print("No ECR repositories found.")

def create_ecr_cli():
    profile_name = input("Enter profile name: ")
    repository_name = input("Enter ECR repository name: ")
    create_ecr_repository(profile_name, repository_name)

def delete_ecr_cli():
    profile_name = input("Enter profile name: ")
    repository_name = input("Enter ECR repository name: ")
    delete_ecr_repository(profile_name, repository_name)

def describe_ecr_cli():
    profile_name = input("Enter profile name: ")
    repository_name = input("Enter ECR repository name: ")
    describe_ecr_repository(profile_name, repository_name)

def ecr_uri_cli():
    profile_name = input("Enter profile name: ")
    repository_name = input("Enter ECR repository name: ")
    uri = get_ecr_repository_uri(profile_name, repository_name)
    print(f"ECR Repository URI for '{repository_name}': {uri}")

def list_s3_cli():
    profile_name = input("Enter profile name: ")
    buckets = list_s3_buckets(profile_name)
    if buckets:
        print(f"S3 Buckets in profile '{profile_name}':")
        for bucket in buckets:
            print(bucket)
    else:
        print(f"No S3 buckets found in profile '{profile_name}'.")

def create_s3_cli():
    profile_name = input("Enter profile name: ")
    bucket_name = input("Enter S3 bucket name: ")
    create_s3_bucket(bucket_name)

def delete_s3_cli():
    profile_name = input("Enter profile name: ")
    bucket_name = input("Enter S3 bucket name: ")
    delete_s3_bucket(bucket_name)

def ec2_ssh_cli():
    if len(sys.argv) < 4:
        print("Usage: haber-devops ec2-ssh <instance_name> <command>")
        return
    instance_name = sys.argv[2]
    ssh_command = sys.argv[3]
    profile_name = input("Enter profile name: ")
    ssh_ec2_instance(profile_name, instance_name, ssh_command)

def rds_cli():
    if len(sys.argv) < 4:
        print("Usage: haber-devops rds <start/stop> <db_instance_identifier>")
        return

    subcommand = sys.argv[2]
    db_instance_identifier = sys.argv[3]
    profile_name = input("Enter profile name: ")

    if subcommand == 'start':
        start_rds_instance(profile_name, db_instance_identifier)
    elif subcommand == 'stop':
        stop_rds_instance(profile_name, db_instance_identifier)
    else:
        print(f"Unknown subcommand: {subcommand}")

def list_rds_cli():
    profile_name = input("Enter profile name: ")
    list_rds_instances(profile_name)

def tag_cli(tag_keyword):
    if len(sys.argv) < 3 or sys.argv[2] != 'ls':
        print(f"Usage: haber-devops {tag_keyword} ls")
        return

    profile_name = input("Enter profile name: ")
    list_resources_by_tag(profile_name, tag_keyword)

def deploy_lambda_cli():
    '''if len(sys.argv) != 4:
        print('Usage: haber-devops deploy <profile_name> <resource_name> <folder_path>')
        sys.exit(1)
    '''
    profile_name = sys.argv[2]
    resource_name = sys.argv[3]
    folder_path = sys.argv[4]
    deploy_cli(profile_name,resource_name,folder_path)



def docker_cli():
    if len(sys.argv) < 3:
        print("Usage: haber-devops docker <command> [options]")
        return
    subcommand = sys.argv[2]

    if subcommand == 'ls':
        docker_ls()
    elif subcommand == 'ps':
        docker_ps()
    elif subcommand == 'stop':
        if len(sys.argv) < 4:
            print("Usage: haber-devops docker stop <container_id>")
            return
        container_id = sys.argv[3]
        docker_stop(container_id)
    elif subcommand == 'sh':
        if len(sys.argv) < 4:
            print("Usage: haber-devops docker sh <container_id>")
            return
        container_id = sys.argv[3]
        docker_sh(container_id)
    elif subcommand == 'run':
        if len(sys.argv) < 6:
            print("Usage: haber-devops docker run <port1> <port2> <image_name>")
            return
        port1 = sys.argv[3]
        port2 = sys.argv[4]
        image_name = sys.argv[5]
        docker_run(port1, port2, image_name)
    else:
        print(f"Unknown Docker subcommand: {subcommand}")

def route53_cli():
    if len(sys.argv) < 3:
        print("Usage: haber-devops route53 <list/create/delete> [options]")
        return
    subcommand = sys.argv[2]

    if subcommand == 'list':
        profile_name = input("Enter profile name: ")
        hosted_zone_id = input("Enter Hosted Zone ID: ")
        list_records(profile_name, hosted_zone_id)
    elif subcommand == 'create':
        profile_name = input("Enter profile name: ")
        hosted_zone_id = input("Enter Hosted Zone ID: ")
        name = input("Enter record name: ")
        record_type = input("Enter record type: ")
        ttl = int(input("Enter TTL: "))
        values = input("Enter record values (comma-separated): ").split(',')
        create_record(profile_name, hosted_zone_id, name, record_type, ttl, values)
    elif subcommand == 'delete':
        profile_name = input("Enter profile name: ")
        hosted_zone_id = input("Enter Hosted Zone ID: ")
        name = input("Enter record name: ")
        record_type = input("Enter record type: ")
        delete_record(profile_name, hosted_zone_id, name, record_type)
    else:
        print(f"Unknown Route 53 subcommand: {subcommand}")

    
if __name__ == "__main__":
    main()