db-local-backup:
	pg_dump --no-owner restaurant_demo > restaurant_demo.dump

db-push-local-to-heroku:
	heroku pg:psql < mydb.dump