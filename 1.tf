resource "aws_security_group" "bad_sg" {
  name        = "open_sg"
  description = "Allow all traffic from the internet"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ 모든 IP 허용
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "open_bucket" {
  bucket = "totally-open-bucket"
  acl    = "public-read"  # ❌ 퍼블릭 읽기
}

resource "aws_iam_user" "leaked" {
  name = "admin-user"
  path = "/"

  tags = {
    aws_access_key = "AKIA123456789FAKE"  # ❌ 하드코딩된 키 유사값
  }
}
