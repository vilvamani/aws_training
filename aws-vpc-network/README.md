# aws-vpc-cloudformation

This Cloudformation templates provides a networking foundation for AWS Cloud infrastructures. It deploys an Amazon Virtual Private Cloud (Amazon VPC) according to AWS best practices and guidelines.

The Amazon VPC architecture includes public and private subnets. A set of private subnets share the default network access control list (ACL) from the Amazon VPC.

![Amazon VPC Architecture](https://github.com/vilvamani/aws_training/blob/master/aws-vpc-network/docs/images/vpc_network_architecture.jpg)

For additional information about these best practices, see the following
documentation:

* http://d0.awsstatic.com/aws-answers/AWS_Single_VPC_Design.pdf[AWS
Single VPC Design] from the AWS Answers website
* http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html[Your
VPC and Subnets] in the Amazon VPC documentation
* https://medium.com/aws-activate-startup-blog/practical-vpc-design-8412e1a18dcc[Practical
VPC Design] in the AWS Startups blog
* http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html[Network
ACLs] in the Amazon VPC documentation