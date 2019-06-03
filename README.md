# Iriversland2

This is the public-facing repository for my personal website which contains my portfolio, case study and bio.

## Update

The site is currently taken down for cost reasons. This single site which uses AWS Elastic Beanstalk and Relational Database Service costs me over $50 a month (load balancer $20+, RDS $15, EC2 $15). A big portion of it is due to the fact that elastic beanstalk by default uses ELB (elastic load balancer), which is now classic load balancer. 

- Terminated elastic beanstalk environment
- Terminated RDS for iriversland2 (also for appl tracky)

I'm finding a way to manage the cost while searching for other hosting alternatives. Several articles indicate that using Application Load Balancer will be much cheaper, based on the cost calculation model of AWS. I will plan to spin up the server again in the near future.


# Reference

- Instructions on setting up [git submodules](/docs)
- Instructions on setting up [enforcing http to https](/docs)