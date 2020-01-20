db-local-backup:
	pg_dump -Fc --no-acl --no-owner -h localhost restaurant_demo > restaurant_demo.dump

