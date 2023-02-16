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


Result
----------------
**1. Fill in the facility name with the same address and fill in the phone number with the same facility name**
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

**2. There is several Null in facility name and phone number. I fill in the value by searching the address on Google.**

```sql
update PortfolioProject.dbo.HepatitisNYC
set FacilityName='Alliance LES Harm Reduction Center',
"Phone Number"= '(212) 645-0875 ext. 100'
Where "Address" = '35 East Broadway'
```
<details><summary>Click for more codes in section 2</summary>
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




**3. The format of phone number looks messy. I want to uniform the forms to (xxx) xxx-xxxx**

*3-1 Change Phone Number XXXXXXXXXX into (XXX) XXX-XXXX*
```sql
update PortfolioProject.dbo.HepatitisNYC
set "Phone Number" = '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 4, 3) + '-' + substring("Phone Number", 7, 3) 
WHERE len("Phone Number")=10
```

*3-2 Change Phone Number XXX-XXX-XXXX into (XXX) XXX-XXXX*
```sql
update PortfolioProject.dbo.HepatitisNYC
Set "phone number" = '(' + substring("Phone Number", 1, 3) + ') ' + substring("Phone Number", 5, 3) + '-' + substring("Phone Number", 9, 3) 
WHERE len("Phone Number")=12

update PortfolioProject.dbo.HepatitisNYC
set"phone number" = '(347) 770-9911 X6309' 
WHERE "Phone Number"='347-770-9911 X6309'
```

*3-3 Uniform the phone number extension format to ext*
```sql
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

*3-4 There are missing number, let's update it*
```sql
SELECT FacilityName, Address, [Phone Number]
FROM PortfolioProject.dbo.HepatitisNYC
WHERE len("Phone Number")<14
order by FacilityName
```
<details><summary>Click for more codes in section 3-4</summary>
<p>

```sql
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
</p>
</details>

**4. Do data aggregation in Payment/Cos. Create a new variable FreeHep,   
if payment contains free option then returns 'yes', if not, returns 'no', else returns 'unknown'.**
```sql
ALTER TABLE PortfolioProject.dbo.HepatitisNYC
ADD FreeHep nvarchar(255)

Update PortfolioProject.dbo.HepatitisNYC
SET FreeHep = case when [Payment/Cost] Like '%Free%' then 'Yes'
when [Payment/Cost] IS NULL then 'Unknown'
Else 'No'
END
FROM PortfolioProject.dbo.HepatitisNYC
```

**5. The forms of Address looks messy. I observe several problems:**  
．There are 'n/a' and NULL  
．Different forms of Floor: 1 st Floor, 1F, 1 floor, 1 Floor 
．Different forms of #: # 307, Room# 336
．Some first characters in the string are uppercase, some are lowercase  

*5-1 Breaking out Address into Individual Columns (Address, apartment/suite number)*
```sql
ALTER TABLE PortfolioProject.dbo.HepatitisNYC
ADD AddressSplitAddress nvarchar(255), AddressSplitSuite nvarchar(255)

UPDATE PortfolioProject.dbo.HepatitisNYC
SET AddressSplitAddress = PARSENAME(REPLACE(Address, ',', '.'),2)
Where [Address] Like '%,%'

UPDATE PortfolioProject.dbo.HepatitisNYC
SET AddressSplitAddress = Address
Where [Address] not Like '%,%'

UPDATE PortfolioProject.dbo.HepatitisNYC
SET AddressSplitSuite = PARSENAME(REPLACE(Address, ',', '.'),1)
Where [Address] Like '%,%'
```
*5-2 Replace n/a in to NULL in AddressSpliteSuite*
```sql
UPDATE PortfolioProject.dbo.HepatitisNYC
SET AddressSplitSuite = replace(AddressSplitSuite,'n/a', NULL)
Where [Address] Like '%n/a%
```

*5-3 Change '1 st floor' and '1F' to '1st Floor'  
and Change '# 307' and 'Room# 336' to '#307' and 'Room#336'*
```sql
UPDATE PortfolioProject.dbo.HepatitisNYC
Set AddressSplitSuite=REPLACE(Replace(AddressSplitSuite, '1 St Floor', '1st Floor'), '1f', '1st Floor')
where  AddressSplitSuite IN ('1 St Floor', '1f')

UPDATE PortfolioProject.dbo.HepatitisNYC
Set AddressSplitSuite=REPLACE(REPLACE(AddressSplitSuite, '# ', '#'), 'Room#', 'Room #')
where  AddressSplitSuite IN ('# 307', 'Room# 336')
```

*5-4 Make the first character of the string into uppercase*  
The reference of the code: http://www.sql-server-helper.com/functions/initcap.aspx

Step 1: Create a Function called "InitCap":  
The function takes in a single input parameter, a varchar data type with a maximum length of 4000 characters, and returns a varchar with the same maximum length.
```sql
CREATE FUNCTION [dbo].[InitCap] ( @InputString varchar(4000) ) 
RETURNS VARCHAR(4000)
AS
BEGIN
```


Step 2: Define variables and specify their data type
```sql
DECLARE @Index          INT
DECLARE @Char           CHAR(1)
DECLARE @PrevChar       CHAR(1)
DECLARE @OutputString   VARCHAR(255)
```

Step 3: Set the value of @OutputString to the lowercase version of the input string and the value of @Index to 1, which is the initial index value that is used to loop through the input string character
```sql
SET @OutputString = LOWER(@InputString)
SET @Index = 1
```

Step 4: Create a While Loop  
--Set the value of @Char to be the character at the current index using the SUBSTRING function
--Set the value of @PrevChar to be the previous character in the string
--Set the value of @PrevChar to be a space if the current character is the first character in the string
```sql
WHILE @Index <= LEN(@InputString)
BEGIN
    SET @Char     = SUBSTRING(@InputString, @Index, 1)
    SET @PrevChar = CASE WHEN @Index = 1 THEN ' '
                         ELSE SUBSTRING(@InputString, @Index - 1, 1)
```

Step 5: IF checks whether the previous character is a space, comma, or hyphen.  
If it is, then it uses the SQL Server "STUFF" function to replace the current character with its uppercase equivalent in the output string
```sql
IF @PrevChar IN (' ', ',','-')
    BEGIN
            SET @OutputString = STUFF(@OutputString, @Index, 1, UPPER(@Char))
    END
```

Step 6: Iterate over the individual words in the input string.  
The loop initializes @Index to 1 and increments it by 1 on each iteration until all the words have been processed.  
The RETURN @OutputString statement indicates that the final output string should be returned when the function is called.  
The GO statement marks the end of the T-SQL batch and is used to separate batches within a script.
```sql
SET @Index = @Index + 1
END
RETURN @OutputString
END
GO
```

Step 7: Apply the function to AddressSplitAddress and AddressSplitSuite
```sql
UPDATE PortfolioProject.dbo.HepatitisNYC
SET AddressSplitSuite = [dbo].[InitCap] ( [AddressSplitSuite] ), AddressSplitAddress = [dbo].[InitCap] ( [AddressSplitAddress] )
```

**6. Remove duplicate data**
```sql
Select FacilityName, "Service Type", Address, "Phone Number", ROW_NUMBER() over (partition by FacilityName, "Service Type", Address, "Phone Number" order by FacilityName) rownum
From PortfolioProject.dbo.HepatitisNYC
order by rownum desc

WITH CTE AS (
SELECT *, ROW_NUMBER() over (partition by FacilityName, "Service Type", Address, "Phone Number" order by FacilityName) as rownum
FROM PortfolioProject.dbo.HepatitisNYC
)
DELETE FROM CTE 
WHERE rownum >1
```

**7. Remove missing value in Facility name**
```sql
DELETE FROM PortfolioProject.dbo.HepatitisNYC
WHERE FacilityName IS NULL OR FacilityName = ''
```


**8. Remove irrevelant data**
```sql
ALTER TABLE PortfolioProject.dbo.HepatitisNYC
DROP COLUMN Address, [Address 2], AdditionalInfo, [Special Populations Served], [Community Board], [City Council], [Census Tract], BIN, BBL 
```
