# aws-vpc-cloudformation

This Cloudformation templates provides a networking foundation for AWS Cloud infrastructures. It deploys an Amazon Virtual Private Cloud (Amazon VPC) according to AWS best practices and guidelines.

The Amazon VPC architecture includes public and private subnets. A set of private subnets share the default network access control list (ACL) from the Amazon VPC.

![Amazon VPC Architecture](https://docs.aws.amazon.com/quickstart/latest/vpc/images/quickstart-vpc-design-fullscreen.png)

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