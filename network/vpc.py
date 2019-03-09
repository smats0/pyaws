import boto3

##Wrappers that instantiate the boto3 Resource....goal is to manipulate AWS Cloud objects


class VPC
	def __init__(self, vpc_id=None):
		self.id = vpc_id
		self.igw_id = None
		self.subnets ={}
		self.route_tables={}


	##Private Methods##
	def _create_client(self, service, aws_access_key_id, aws_secret_access_key, region=None):
		_session = boto.session.Session()
		_client = _session.client(service, aws_access_key_id, aws_secret_access_key, region_name=region)
		return _client


	def _create_igateway(self):
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)
		igw = client.create_internet_gateway()
		del client
		return igw['InternetGateway']['InternetGatewayId']



	##Public Methods##
	def create_vpc(self, ipv4_cidr, enable_ipv6=False, name=None):
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)
		vpc = client.create_vpc(CidrBlock=ipv4_cidr, AmazonProvidedIpv6CidrBlock=enable_ipv6, DryRun=True)
		waiter = client.get_waiter('vpc_available')
		waiter.wait()
		del client
		self.id = vpc['Vpc']['VpcId']


	def attach_igateway(self, igateway_id=None)
		if igateway_id != None:
			self.igw_id = igateway_id
		else:
			self.igw_id = self._create_igateway()
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)
		waiter = client.get_waiter('vpc_exists')
		waiter.wait()
		client.attach_internet_gateway(InternetGatewayId=self.igw_id, VpcId=self.id, DryRun=True)			
		del client
	
	def detach_igateway(self, igateway_id=None):
		client = _create_client('ec2', aws_access_key_id, aws_secret_access_key)
		if igateway_id == None:
			response = client.detach_internet_gateway(InternetGatewayId=self.igw_id, VpcId=self.id, DryRun=True)
		else:
			response = client.detach_internet_gateway(InternetGatewayId=igateway_id, VpcId=self.id, DryRun=True)
		self.igw_id == None
		del client



	##TODO:## 
	def get_subnets(self):
		return list_subnet_ids

	def create_subnet(self, ipv4_cidr, ipv6_cidr=None, azone=None, name=None)
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)
		waiter = client.get_waiter('vpc_available')
		waiter.wait()
		subnet = client.create_subnet(AvailabilityZone=azone, CidrBlock=ipv4_cidr, Ipv6CidrBlock=ipv6_cidr, VpcId=self.id, DryRun=True)
		waiter = client.get_waiter('subnet_available')
		waiter.wait()
		self.subnet_ids.add(subnet['Subnet']['SubnetId'])
		del client

	def delete_subnet(self, subnet_id):
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)
		client.delete_subnet(SubnetId=subnet_id,DryRun=True)
		self.subnet_ids.discard(subnet_id)
		del client




	def create_route_table(self, name=None):
		client = self.create_client('ec2', aws_access_key_id, aws_secret_access_key)
		route_table = client.create_route_table(VpcId=self.id, DryRun=True)
		route_table_id = route_table['RouteTable']['RouteTableId']
		self.route_tables.add(route_table_id)
		del client

	def set_routes(self, route_table_id, route_map):
		client = self._create_client('ec2', aws_access_key_id, aws_secret_access_key)




	def associate_route_table(self, ):
		client = self.create_client('ec2', aws_access_key_id, aws_secret_access_key)



	def attach_route_table(self, route_table_id, subnet_id):
	def detach_route_table(self, route_table_id, subnet_id):
	def set_routes(self, route_table_id, route_map):
	def reset_route_table(self, ):


	def create_natgateway(self):






