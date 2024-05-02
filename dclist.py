#!/usr/bin/env python3
# list all running containers ip. accept name or short-id for single container ip output.
import docker
import sys
from operator import itemgetter

def formatted_output(containers):
    fmt = "{0:<25}{1:<12}{2}"
    print(fmt.format("Name", "Short ID", "IP Address"))
    for container in containers:
        ip_addresses = ', '.join([net['IPAddress'] for net in container.attrs['NetworkSettings']['Networks'].values()])
        print(fmt.format(container.name, container.short_id, ip_addresses))


def list_containers():
    client = docker.from_env()
    containers = client.containers.list() # If you want to include stopped, set (all=True).
    formatted_output(containers)

def inspect_container(container):
    client = docker.from_env()

    try:
        if len(container) == 12 and all(c.isalnum() or c == '-' for c in container):  # if it's a short id, check this first
            container = client.containers.get(container)
        else:
            containers = [c for c in client.containers.list() if c.name == container or c.short_id == container]
            formatted_output(containers)

    except docker.errors.NotFound as e:
        print(str(e))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        list_containers()
    else:
        inspect_container(sys.argv[1])
