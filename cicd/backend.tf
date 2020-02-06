terraform {
  backend "s3" {
    bucket = "iriversland-cloud-state"
    key    = "terraform/iriversland2-api.remote-terraform.tfstate"
  }
}
