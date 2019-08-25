# Iriversland2 Backend API

[![CircleCI](https://circleci.com/gh/rivernews/iriversland2-public/tree/master.svg?style=shield)](https://circleci.com/gh/rivernews/iriversland2-public/tree/master)

This is the public-facing repository for my personal website which contains my portfolio, case study and bio.

## Update

**(Aug 2019)

The site is migrated from AWS Elastic beanstalk stack, to a kubernetes cluster on digital ocean w/ a CI/CD setup using CircleCI. Please [refer to Kubernetes & CI/CD Architecture Overview README](docs/cicd-archi-overview.md) for details.

**(May 2019)

The site is currently taken down for cost reasons. This single site which uses AWS Elastic Beanstalk and Relational Database Service costs me over $50 a month (load balancer $20+, RDS $15, EC2 $15). A big portion of it is due to the fact that elastic beanstalk by default uses ELB (elastic load balancer), which is now classic load balancer. 

- Terminated elastic beanstalk environment
- Terminated RDS for iriversland2 (also for appl tracky)
    - Stored snapshot available on RDS.

I'm finding a way to manage the cost while searching for other hosting alternatives. Several articles indicate that using Application Load Balancer will be much cheaper, based on the cost calculation model of AWS. I will plan to spin up the server again in the near future.

## What's left undone

Check out the [Roadmap v0.6](https://github.com/rivernews/iriversland2-public/wiki/Roadmap-v0.6) wiki page.

## Database

As of August 4, 2019, the app switches from using AWS RDS to Heroku.

Since it's a production site now, database contents needs to be backup. According to the [heroku doc](https://devcenter.heroku.com/articles/heroku-postgres-backups):

- Backup the database: go to web portal, click `Create Manual Backup`. Max of 2 backups.
    - Can also consider downloading the backup to get rid of the 2 backup limitation, like storing it on S3. But currently, will be just using the manual 2 backups.
    - Future work: add some sort of scheduled automation to do the backup.
- [Restore](heroku pg:backups:restore b101 DATABASE_URL --app sushi): 
    - Will need heroku cli. (of course `psql` may work too, but just for sake of simplicity)
    - `heroku pg:backups:restore <the name of backup like b101> DATABASE_URL --app <the app name like iriversland2-public>`

# Reference

- Instructions on setting up [git submodules](/docs)
- Instructions on setting up [enforcing http to https](/docs)