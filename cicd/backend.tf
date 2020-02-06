terraform {
  backend "s3" {
    bucket = "iriversland-cloud"
    key    = "terraform/iriversland2-api.remote-terraform.tfstate"
  }
}
