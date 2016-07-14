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

License
-------

BSD

Author Information
------------------

- Zacharias Thompson <zarlant@gmail.com>
