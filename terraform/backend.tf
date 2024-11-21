terraform {
  backend "s3" {
    bucket         = "dami-cde-bucket"
    key            = "dev/dev.tfstate"
    region         = "eu-north-1"
    encrypt        = true
  }
}