import sys
import MerakiAPI
import requests
import json
import pprint


#### MerakiAPI Courtesy of Meraki Dev team
#### Demo Application John Shea Cisco Systems 2017

print("******************************")
print("*   Meraki API Demo Script   *")
print("*       Multi Feature        *")
print("*.                           *")
print("******************************")

#comment out the below input lines and uncomment the static assignment section if you do not wish to be prompted
apikey = input("Please Enter Your API Key: ")
orgid = input("Please Enter Your ORG ID: ")
netid = input("Please Enter Your Network ID: ")

#Static value assignment <insert value into fields>
#apikey = str("<insert here>")
#orgid = str("<insert here>")
#netid = str("<insert here>")

#start Menu
def print_menu():
	print (30 * "-" , "API Demo Menu" , 30 * "-")
	print ("1. Get Orginization ID")
	print ("2. Get Network IDs")
	print ("3. Get Vlan Information")
	print ("4. Get Network Device Inventory")
	print ("5. Get Network Details")
	print ("6. Create a Wirless Network")
	#print ("7. Claim a Serial #")
	#print ("8. Assign a Device to a Network")
	print ("100. Exit")


#Start Options Loop: info accuracy is important I have not written error handlers yet
loop=True
while loop:
	print_menu()
	choice = input("Please Enter Your Selection: ")
	choice=int(choice)
	if choice==1:
		try:
			dataset = MerakiAPI.myorgaccess(apikey)
			print("You have access to the following Orginizations: ")
			print("----------------------------------------------- ")
			pprint.pprint(dataset)
			print()
		except:
			pass

	elif choice==2:
		try:
			dataset = MerakiAPI.getnetworklist(apikey, orgid)
			pprint.pprint(dataset)
		except:
			pass



	elif choice==3:
		print ("Retrieving Orginization Network Information")
		dataset = MerakiAPI.getnetworklist(apikey, orgid)
		for row in dataset:
			vlans = MerakiAPI.getvlans(apikey, row['id'])
			try:
				print('VLAN Details for Network ID {0}'.format(str(row['id'])))
				for vlanrow in vlans:
					vlaninfo = MerakiAPI.getvlandetail(apikey, row['id'], vlanrow['id'])
					print(vlaninfo, end='\n')
			except:
				pass
	elif choice==4:
		print('Getting Device Inventory for Network ID - {0}'.format(netid))
		print("-----------------------------------------------------------")
		dataset = MerakiAPI.getnetworkdevices(apikey, netid)
		for row in dataset:
			try:
				pprint.pprint(dataset)
				print("-----------------------------------")
				#print (row, end='\n')
				
			except:
				pass	
		
		#print(dataset)

	elif choice==5:
		print('Getting Network Detail for ORG ID - {0}'.format(netid))
		print("-----------------------------------------------------------")
		dataset = MerakiAPI.getnetworkdetail(apikey, netid)
		#for row in dataset:
		#	try:
		#		print("---------------------------------------------------")
		#		print (row)
		#	except:
		#		pass
		len(dataset)
		pprint.pprint(dataset)

	elif choice==6:
		newnet = input("Please enter the value for the new wireless network: ")
		newnet = str(newnet)
		nettype = input("Please enter the network type (Wireless, Switch, Security Appliance)")
		nettype = str(nettype)
		tags = input("Please enter an initial tag for this network")
		tags = str(tags)
		tz = str("EST")
		netinput = MerakiAPI.addnetwork(apikey, orgid, newnet, nettype, tags, tz)
		print("Wireless Network {0}, has been added to ORG ID: {1}".format(str(newnet), str(orgid)))
		pprint.pprint(netinput)


	elif choice==100:
		loop=False
		break
	else:
		input("Press any key to continue...")
