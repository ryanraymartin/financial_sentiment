NOTES FOR CONFIGURING AWS FOR RAY CLUSTER:

1. Create roles to assign to head/worker nodes

In terminal:

vim example-role-trust-policy.json

Then, create role with trust policy for user on ray-head (do the same with ray-worker):

aws iam create-role --role-name ray-head-v1 --assume-role-policy-document file://example-role-trust-policy.json

2. Create instance profile, and assign role to it (do also for ray-worker)

aws iam create-instance-profile --instance-profile-name ray-head-v1
aws iam add-role-to-instance-profile --instance-profile-name ray-head-v1 --role-name ray-head-v1

Double-check here: 

For one:
aws iam list-instance-profiles | grep ray-head-v1

For both:
aws iam list-instance-profiles

3. After creating policies for EC2 and S3, assign policies to roles

ray-head-v1 is assigned both:
aws iam attach-role-policy --policy-arn arn:aws:iam::293752409801:policy/ray-ec2-launcher --role-name ray-head-v1
aws iam attach-role-policy --policy-arn arn:aws:iam::293752409801:policy/ray-s3-access --role-name ray-head-v1

ray-worker-v1 is only assigned s3:
aws iam attach-role-policy --policy-arn arn:aws:iam::293752409801:policy/ray-s3-access --role-name ray-worker-v1


4. 
