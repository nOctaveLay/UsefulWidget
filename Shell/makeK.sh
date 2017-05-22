#!/bin/bash
if ls -al ~/.ssh/id_rsa.pub
then 
	echo "Done"
	vi ~/.ssh/id_rsa
else
	ssh-keygen -t rsa 
	eval "$(ssh~gent -s)" 
	ssh-add ~/.ssh/id_rsa
	vi ~/.ssh/id_rsa
fi
exit
