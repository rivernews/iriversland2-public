# Building a CI/CD pipeline for Django App Running on Kubernetes

## Walkthrough & Key Tech Stacks

This project uses resources that spread across different stack and cloud providers. The biggest motivator for choosing these stack is for cost reasons. Overall, we should be able to achieve a monthly cost of $10 for the Kubernetes cluster on Digital Ocean, plus a yearly cost of around $10 for keeping the domain.

1. **Github**: code commit
1. **CircleCI**: Master branch triggers CircleCI to start build process
    1. Phase I: **Dockerfile**: build the **Django** app images, and push to **Dockerhub** image registry.
    1. Phase 2: **Terraform**: run terraform script to update kubernetes deployment for applying the code changes on production server. The **Kubernetes** cluster is provided by **Digital Ocean**.
1. Access Django app by the published domain name, whose root domain is purchased via AWS **Route53**.
    1. We use database on **Heroku** to save cost.
    1. We use **AWS S3** to serve the frontend code base.
1. Secret management - we use **AWS SSM parameter store**.

## Key Configurations

1. Github repository setup
1. CircleCI
    1. Associate w/ github repository
    1. Add environment variables on CircleCI web portal
1. Dockerize Django App & Dockerhub Registry
    1. Writing Dockerfile for production
    1. (writing dockerfile for local development)
1. Terraform to provision and update the Kubernetes infrastructure on Digital Ocean
    1. Provision the cluster
    1. Provision ingress
    1. Provision external DNS and link that to our Route53 domain name.
1. Manage secrets via AWS SSM parameter store, by using Terraform.

## Motivation

1. Cost on AWS: hard to track and keep control of making max use of resources.
1. Will-expire credits on main stream cloude provider is not a permanent solution when it comes to saving cost.