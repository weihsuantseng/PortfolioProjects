Data Cleaning of Hepatitis NYC
=====================
<img width="400" alt="image" src="https://user-images.githubusercontent.com/122644015/219136467-3a0fb32d-8e1e-4b9c-aaf9-c125571e680f.png">

Data Source
-----------------
[DOHMH Health Map - Hepatitis](https://data.cityofnewyork.us/Health/DOHMH-Health-Map-Hepatitis/nk7g-qeep)  

Goal
----------------
I want to create a map that shows the locations of hepatitis services in New York City.  
The variables I focused on includes: States, FacilityName, ServiceCategory, ServiceType, Address, Country, Postcode, Phone Number, Payment/Cost.  
Before creating a visualization in Tableau, let's perform some data cleaning using SQL server!  


3. Fix structural errors
4. Handle missing data
1. Remove irrelevant data
2. Remove duplicate data

Result
----------------
1. Fill in the facility name with the same address and fill in the phone number with the same facility name
```sql
update a
set FacilityName = ISNULL(a.FacilityName, b.FacilityName)
From PortfolioProject.dbo.HepatitisNYC a
Join PortfolioProject.dbo.HepatitisNYC b
on a.address= b.address and a.Latitude = b.Latitude
where a.FacilityName is NULL

update a
set "phone number" = ISNULL(a."phone number", b."phone number")
From PortfolioProject.dbo.HepatitisNYC a
Join PortfolioProject.dbo.HepatitisNYC b
on a.FacilityName= b.FacilityName and a.Latitude = b.Latitude
where a."phone number" is NULL
```

2. There is several Null in facility name and phone number. I fill in the value by searching the address on Google.
```sql
update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Alliance LES Harm Reduction Center',
"Phone Number"= '(212) 645-0875 ext. 100'
Where "Address" = '35 East Broadway'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - Clay Avenue Family Health Center',
"Phone Number"= '(718) 684-9422'
Where "Address" = '1776 Clay Avenue'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - BASICS Community Health Center',
"Phone Number"= '(718) 861-5650'
Where "Address" = '1064 Franklin Avenue'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - Claremont Family Health Center'
, "Phone Number"= '(718) 734-2539'
Where "Address" = '262 East 174 Street'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - Park Avenue Family Health Center'
, "Phone Number"= '(718) 734-2539'
Where "Address" = '4196 Park Avenue'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - Westchester Avenue Family Health Center'
, "Phone Number"= '(718) 466-3550'
Where "Address" = '915 Westchester Avenue'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Montefiore - The University Hospital for Albert Einstein College of Medicine'
, "Phone Number"= '(718) 904-2000'
Where "Address" = '111 East 210 Street'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Fort Greene Health Center'
, "Phone Number"= '(347) 396-7943'
Where "Address" = '295 Flatbush Avenue Extension'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Acacia Network - Clay Avenue Family Health Center'
, "Phone Number"= '(718) 684-9422'
Where "Address" = '4721 Ft Hamilton Parkway'

update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Elizabeth Seton Pediatric Center',
Address= '300 Corporate Blvd S',
Postcode='10701',
Country='Yonkers',
Latitude=43.884441,
Longitude=-111.668022
Where "Phone Number" = '(212) 239-6586'
```

