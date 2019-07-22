# https://www.terraform.io/docs/configuration/variables.html#variable-definitions-tfvars-files

variable "do_cluster_name" {}

variable "app_container_image" {}

variable "cicd_namespace" {}

variable "app_label" {}

variable "app_name" {}

variable "app_exposed_port" {}

variable "managed_route53_zone_name" {}
variable "managed_k8_external_dns_domain" {}

variable "app_deployed_domain" {}



# CREDENTIALS
#
#
variable "do_token" {}

variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "aws_region" {}



variable "docker_registry_url" {}
variable "docker_email" {}
variable "docker_username" {}
variable "docker_password" {}