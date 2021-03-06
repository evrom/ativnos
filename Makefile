# ssh server alias
SERVER=ativnos

# copy secret production environment files to server
copy_env:
	rsync -r .envs $(SERVER):/var/app

# pull latest git source and restart service
update:
	ssh $(SERVER) '/bin/sh /var/app/deploy/update.sh'

yapf:
	yapf -r -i --style=pep8 ./ativnos

isort:
	isort -rc ./ativnos

format_python: yapf isort



