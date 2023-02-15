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
```
<details><summary>Click for more code in section 2</summary>
<p>

```sql
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
</p>
</details>




3. The format of phone number looks messy. I want to uniform the format to (xxx) xxx-xxxx

```sql
--Change Phone Number XXXXXXXXXX into (XXX) XXX-XXXX format
SELECT "phone number", '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 4, 3) + '-' + substring("Phone Number", 7, 3) AS new_phone_number
FROM PortfolioProject.dbo.HepatitisNYC
WHERE len("Phone Number")=12

update PortfolioProject.dbo.HepatitisNYC
set "Phone Number" = '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 4, 3) + '-' + substring("Phone Number", 7, 3) 
WHERE len("Phone Number")=10
```

```sql
--Change Phone Number XXX-XXX-XXXX into (XXX) XXX-XXXX format
SELECT "phone number", '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 5, 3) + '-' + substring("Phone Number", 9, 3) AS new_phone_number
FROM PortfolioProject.dbo.HepatitisNYC
WHERE len("Phone Number")=12

update PortfolioProject.dbo.HepatitisNYC
Set "phone number" = '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 5, 3) + '-' + substring("Phone Number", 9, 3) 
WHERE len("Phone Number")=12

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(347) 770-9911 X6309' 
WHERE "Phone Number"='347-770-9911 X6309'
```

```sql
--There are missing number, let's update it--
SELECT FacilityName, Address, [Phone Number]
FROM PortfolioProject.dbo.HepatitisNYC
WHERE len("Phone Number")<14
order by FacilityName

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 334-6029' 
WHERE "Phone Number"='(646) 744-098'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 334-6029' 
WHERE "Phone Number"='(646)744-0985'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(646) 602-6404' 
WHERE "Phone Number"='(646) 602-640'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(718) 328-4188' 
WHERE "Phone Number"='(718) 328-418'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(718) 945-7150', FacilityName ='The Joseph P. Addabbo Family Health Center, Inc.'
WHERE "Phone Number"='(718) 945-715'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(718) 277-0386', FacilityName ='Housing Works - Keith D. Cylar Community Health Center'
WHERE "Phone Number"='(212) 677-799'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 206-0574', FacilityName ='Housing Works - Keith D. Cylar Community Health Center'
WHERE "Phone Number"='(212) 677-799'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 206-0574'
WHERE "Phone Number"='(718) 469-736'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(718) 277-0386'
WHERE "Phone Number"='(347) 949-197'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 749-1820'
WHERE "Phone Number"='(212) 531-755'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(212) 695-2220'
WHERE "Phone Number"='(212) 695-222'

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(718) 583-5150 / (718) 466-8244'
WHERE "Phone Number"='(718) 583-5150 / 718-466-8244'
```

```sql
--Uniform the phone number extension format to ext.
SELECT*
FROM PortfolioProject.dbo.HepatitisNYC
WHERE len("Phone Number") != 14
order by FacilityName

SELECT [Phone Number], replace([Phone Number], 'X', 'ext. ')
FROM PortfolioProject.dbo.HepatitisNYC
WHERE [Phone Number] LIKE '%X%' and [Phone Number] not LIKE '%ext.%'

Update PortfolioProject.dbo.HepatitisNYC
Set [Phone Number] = replace([Phone Number], 'X', 'ext. ')
WHERE [Phone Number] LIKE '%X%' and [Phone Number] not LIKE '%ext.%'
```