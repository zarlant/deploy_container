Deploy Container
=========

Deploys a container to docker hosts

Requirements
------------

Requires docker-py, which will be installed on the host by the role.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.


Example Playbook
----------------

	- name: Ensure containers are running
	  hosts: "docker-{{env}}"
	  vars_files:
	   - vars/main.yml
	   - "vars/{{env}}_secrets.yml"
	   - "vars/{{env}}_config.yml"
	  roles:
	    - { role: deploy_container, tags: docker }
	  vars:
	    - containers: "{{ default_containers | merge_lists(other_containers) }}" 

Example Variables
-----------------

Example variables file to ensure consul and registrator are running on the host:

	consul_user: 100
	consul_group: docker
	congo_containers:
	default_containers:
	  - docker_registry: ""
	    container_name: consul
	    application_name: consul
	    container_tag: latest
	    log_driver: "journald"
	    container_network_mode: host
	    container_volumes:
	      - "{{ consul_data_directory }}:{{ consul_data_directory }}:rw"
	      - "{{ consul_server_config_path }}:/consul/config"
	    container_command:
	      - "agent"
	      - "-config-dir=/consul/config"
	    container_env:
	      CONSUL_LOCAL_CONFIG: "{\"skip_leave_on_interrupt\": true}"
	  - docker_registry: ""
	    container_name: gliderlabs/registrator
	    application_name: registrator
	    container_tag: latest
	    log_driver: "journald"
	    container_network_mode: host
	    container_volumes: /var/run/docker.sock:/tmp/docker.sock
	    container_command:
	      - "-ip={{ansible_default_ipv4.address}}"
	      - "consul://{{ansible_default_ipv4.address}}:8500"


License
-------

BSD

Author Information
------------------

- Zacharias Thompson <zarlant@gmail.com>
