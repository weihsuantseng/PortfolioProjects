$ jupyter nbconvert --to html mynotebook.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ef1d70df",
   "metadata": {},
   "source": [
    "# Exploring the NYC Airbnb Market"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd7cdaa3",
   "metadata": {},
   "source": [
    "<img src=\"https://user-images.githubusercontent.com/122644015/219280337-68365f68-76bc-422f-8289-0f537d8898e2.png\" width=\"400\">"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e10a0d5",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "This is a datacamp project.  \n",
    "In this project, I will apply data importing and cleaning skills to uncover insights about the Airbnb market in New York City."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "928b35be",
   "metadata": {},
   "source": [
    "Goal\n",
    "-------------------------------\n",
    "1. Importing the Data\n",
    "2. Cleaning the price column\n",
    "3. Calculating average price\n",
    "4. Comparing costs to the private rental market\n",
    "5. Cleaning the room type column\n",
    "6. What timeframe are we working with?\n",
    "7. Joining the DataFrames.\n",
    "8. Analyzing listing prices by NYC borough\n",
    "9. Price range by borough"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "237efeb8",
   "metadata": {},
   "source": [
    "## 1. Importing the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "de416130",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Python library\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dde56d94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   listing_id        price                nbhood_full\n",
      "0        2595  225 dollars         Manhattan, Midtown\n",
      "1        3831   89 dollars     Brooklyn, Clinton Hill\n",
      "2        5099  200 dollars     Manhattan, Murray Hill\n",
      "3        5178   79 dollars  Manhattan, Hell's Kitchen\n",
      "4        5238  150 dollars       Manhattan, Chinatown \n",
      "    listing_id                                description        room_type\n",
      "0        2595                      Skylit Midtown Castle  Entire home/apt\n",
      "1        3831            Cozy Entire Floor of Brownstone  Entire home/apt\n",
      "2        5099  Large Cozy 1 BR Apartment In Midtown East  Entire home/apt\n",
      "3        5178            Large Furnished Room Near B'way     private room\n",
      "4        5238         Cute & Cozy Lower East Side 1 bdrm  Entire home/apt \n",
      "    listing_id    host_name   last_review\n",
      "0        2595     Jennifer   May 21 2019\n",
      "1        3831  LisaRoxanne  July 05 2019\n",
      "2        5099        Chris  June 22 2019\n",
      "3        5178     Shunichi  June 24 2019\n",
      "4        5238          Ben  June 09 2019\n"
     ]
    }
   ],
   "source": [
    "#Read Files\n",
    "prices = pd.read_csv(r'C:\\Users\\Wei Hsuan\\Desktop\\Programming\\Portfolio\\Exploring the NYC Airbnb Market\\datasets\\airbnb_price.csv')\n",
    "xls = pd.ExcelFile(r'C:\\Users\\Wei Hsuan\\Desktop\\Programming\\Portfolio\\Exploring the NYC Airbnb Market\\datasets\\airbnb_room_type.xlsx')\n",
    "reviews = pd.read_csv(r\"C:\\Users\\Wei Hsuan\\Desktop\\Programming\\Portfolio\\Exploring the NYC Airbnb Market\\datasets\\airbnb_last_review.tsv\", sep=\"\\t\")\n",
    "#Read the first sheet of xls, room_types\n",
    "room_types=xls.parse(0)\n",
    "\n",
    "#Read the first 5 rows of the data frames\n",
    "print(prices.head(), \"\\n\", room_types.head(), \"\\n\", reviews.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2b98af1",
   "metadata": {},
   "source": [
    "## 2. Cleaning the price column\n",
    "Take a look at the price column. There are messy strings:   \n",
    "*price  \n",
    "225 dollars  \n",
    "89 dollars  \n",
    "200 dollars*  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8dfb468a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method NDFrame.describe of 0        225\n",
      "1         89\n",
      "2        200\n",
      "3         79\n",
      "4        150\n",
      "        ... \n",
      "25204    129\n",
      "25205     45\n",
      "25206    235\n",
      "25207    100\n",
      "25208     30\n",
      "Name: price, Length: 25209, dtype: int64>\n"
     ]
    }
   ],
   "source": [
    "# Remove \"dollars\" from prices column\n",
    "prices[\"price\"] = prices[\"price\"].str.replace(\" dollars\", \"\")\n",
    "\n",
    "\n",
    "# Convert prices column to numeric datatype\n",
    "prices[\"price\"] = pd.to_numeric(prices[\"price\"])\n",
    "\n",
    "\n",
    "# Print descriptive statistics for the price column\n",
    "print(prices[\"price\"].describe)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cee21b3",
   "metadata": {},
   "source": [
    "## 3. Calculating average price\n",
    "Some of listings are actually showing as free. Let's remove these from the DataFrame, and calculate the average price."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7b3afda5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average price per night for an Airbnb listing in NYC is $141.82.\n"
     ]
    }
   ],
   "source": [
    "# Subset prices for listings costing $0, free_listings\n",
    "free_listings = prices[\"price\"]==0\n",
    "\n",
    "# Update prices by removing all free listings from prices\n",
    "prices = prices.loc[~free_listings]\n",
    "\n",
    "# Calculate the average price, avg_price\n",
    "avg_price = round(prices[\"price\"].mean(),2)\n",
    "\n",
    "# Print the average price\n",
    "print(\"The average price per night for an Airbnb listing in NYC is ${}.\".format(avg_price))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70caa1d7",
   "metadata": {},
   "source": [
    "## 4. Comparing costs to the private rental market\n",
    "A 1 bedroom apartment in New York City costs, on average, $3,100 per month.  \n",
    "Let's convert the per night prices of our listings into monthly costs, so we can compare to the private market."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c4397bcb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Airbnb monthly costs are $4313.61, while in the private market you would pay $3,100.00.\n"
     ]
    }
   ],
   "source": [
    "# Add a new column, price_per_month\n",
    "prices[\"price_per_month\"] = prices[\"price\"] *365 / 12\n",
    "\n",
    "# Calculate average_price_per_month\n",
    "average_price_per_month = round(prices[\"price_per_month\"].mean(), 2)\n",
    "\n",
    "# Compare Airbnb and rental market\n",
    "print(\"Airbnb monthly costs are ${}, while in the private market you would pay {}.\".format(average_price_per_month, \"$3,100.00\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b106a7a0",
   "metadata": {},
   "source": [
    "## 5. Cleaning the room type column\n",
    "For private room listings, the room type column comes in a variety of forms, specifically:  \n",
    "\"Private room\"  \n",
    "\"private room\"  \n",
    "\"PRIVATE ROOM\"  \n",
    "By changing all string characters to lower case, we can resolve issue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d90c66f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entire home/apt    13266\n",
      "private room       11356\n",
      "shared room          587\n",
      "Name: room_type, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Convert the room_type column to lowercase\n",
    "room_types[\"room_type\"] = room_types[\"room_type\"].str.lower()\n",
    "\n",
    "# Update the room_type column to category data type\n",
    "room_types[\"room_type\"] = room_types[\"room_type\"].astype(\"category\")\n",
    "\n",
    "# Create the variable room_frequencies\n",
    "room_frequencies = room_types[\"room_type\"].value_counts()\n",
    "\n",
    "# Print room_frequencies\n",
    "print(room_frequencies)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac802aed",
   "metadata": {},
   "source": [
    "## 6. What timeframe are we working with?\n",
    "It seems there is a fairly similar sized market opportunity for both private rooms (45% of listings) and entire homes/apartments (52%) on the Airbnb platform in NYC.\n",
    "\n",
    "\n",
    "Now let's turn our attention to the reviews DataFrame. The last_review column contains the date of the last review in the format of \"Month Day Year\" e.g., May 21 2019. We've been asked to find out the earliest and latest review dates in the DataFrame, and ensure the format allows this analysis to be easily conducted going forwards."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2ed032a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The earliest Airbnb review is 2019-01-01, the latest review is 2019-07-09\n"
     ]
    }
   ],
   "source": [
    "# Change the data type of the last_review column to datetime\n",
    "reviews[\"last_review\"] = pd.to_datetime(reviews[\"last_review\"])\n",
    "\n",
    "# Create first_reviewed, the earliest review date\n",
    "first_reviewed = reviews[\"last_review\"].dt.date.min()\n",
    "\n",
    "# Create last_reviewed, the most recent review date\n",
    "last_reviewed = reviews[\"last_review\"].dt.date.max()\n",
    "\n",
    "# Print the oldest and newest reviews from the DataFrame\n",
    "print(\"The earliest Airbnb review is {}, the latest review is {}\".format(first_reviewed, last_reviewed))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b8fd08c",
   "metadata": {},
   "source": [
    "## 7. Joining the DataFrames.\n",
    "Now that we have extracted the necessary information, we can merge the three DataFrames to make future analyses easier to conduct. After joining the data, we will remove any observations with missing values and check for duplicates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "539ffbff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 0 duplicates in the DataFrame.\n"
     ]
    }
   ],
   "source": [
    "# Merge prices and room_types to create rooms_and_prices\n",
    "rooms_and_prices = prices.merge(room_types, how=\"outer\", on=\"listing_id\")\n",
    "\n",
    "# Merge rooms_and_prices with the reviews DataFrame to create airbnb_merged\n",
    "airbnb_merged = rooms_and_prices.merge(reviews, how=\"outer\", on=\"listing_id\")\n",
    "\n",
    "# Drop missing values from airbnb_merged\n",
    "airbnb_merged.dropna(inplace=True)\n",
    "\n",
    "# Check if there are any duplicate values\n",
    "print(\"There are {} duplicates in the DataFrame.\".format(airbnb_merged.duplicated().sum()))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f1db71e",
   "metadata": {},
   "source": [
    "## 8. Analyzing listing prices by NYC borough\n",
    "Now that we have combined all data into a single DataFrame, let's turn our attention to understanding the difference in listing prices between New York City boroughs. Boroughs are currently listed as the first part of a string within the nbhood_full column, such as:\n",
    "Manhattan, Midtown\n",
    "Brooklyn, Clinton Hill\n",
    "Manhattan, Murray Hill\n",
    "Manhattan, Hell's Kitchen\n",
    "Manhattan, Chinatown\n",
    "\n",
    "Therefore, we need to extract this information from the string and store it in a new column named \"borough\" for analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "650c665a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     sum    mean  median  count\n",
      "borough                                        \n",
      "Manhattan      1898417.0  184.04   149.0  10315\n",
      "Brooklyn       1275250.0  122.02    95.0  10451\n",
      "Queens          320715.0   92.83    70.0   3455\n",
      "Staten Island    22974.0   86.04    71.0    267\n",
      "Bronx            55156.0   79.25    65.0    696\n"
     ]
    }
   ],
   "source": [
    "# Extract information from the nbhood_full column and store as a new column, borough\n",
    "airbnb_merged[\"borough\"] = airbnb_merged[\"nbhood_full\"].str.partition(\",\")[0]\n",
    "\n",
    "# Group by borough and calculate summary statistics\n",
    "boroughs = airbnb_merged.groupby(\"borough\")[\"price\"].agg([\"sum\", \"mean\", \"median\", \"count\"])\n",
    "\n",
    "# Round boroughs to 2 decimal places, and sort by mean in descending order\n",
    "boroughs = boroughs.round(2).sort_values(\"mean\", ascending=False)\n",
    "\n",
    "# Print boroughs\n",
    "print(boroughs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04da6a7b",
   "metadata": {},
   "source": [
    "## 9. Price range by borough\n",
    "The above output provides a summary of prices for Airbnb listings across the five New York City boroughs. To gain further insights, we would like to categorize listings based on their price range and analyze them by borough.\n",
    "\n",
    "To achieve this, we first create a new column, \"price_range\", using percentiles and labels. We then group the data by borough and count the frequencies of listings in each price range. This allows us to see how the distribution of listings varies across the boroughs and gain a more detailed understanding of the New York City Airbnb market."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "133e62f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "borough        price_range\n",
      "Bronx          Budget          381\n",
      "               Average         285\n",
      "               Expensive        25\n",
      "               Extravagant       5\n",
      "Brooklyn       Budget         3194\n",
      "               Average        5532\n",
      "               Expensive      1466\n",
      "               Extravagant     259\n",
      "Manhattan      Budget         1148\n",
      "               Average        5285\n",
      "               Expensive      3072\n",
      "               Extravagant     810\n",
      "Queens         Budget         1631\n",
      "               Average        1505\n",
      "               Expensive       291\n",
      "               Extravagant      28\n",
      "Staten Island  Budget          124\n",
      "               Average         123\n",
      "               Expensive        20\n",
      "               Extravagant       0\n",
      "Name: price_range, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Create labels for the price range, label_names\n",
    "label_names = [\"Budget\", \"Average\", \"Expensive\", \"Extravagant\"]\n",
    "\n",
    "# Create the label ranges, ranges\n",
    "ranges = [0, 69, 175, 350, np.inf]\n",
    "\n",
    "# Insert new column, price_range, into DataFrame\n",
    "airbnb_merged[\"price_range\"] = pd.cut(airbnb_merged[\"price\"], bins=ranges, labels=label_names)\n",
    "\n",
    "# Calculate occurence frequencies for each label, prices_by_borough\n",
    "prices_by_borough = airbnb_merged.groupby([\"borough\", \"price_range\"])[\"price_range\"].count()\n",
    "print(prices_by_borough)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d0d23d44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0        Expensive\n",
      "1          Average\n",
      "2        Expensive\n",
      "3          Average\n",
      "4          Average\n",
      "           ...    \n",
      "25197      Average\n",
      "25198       Budget\n",
      "25199    Expensive\n",
      "25200      Average\n",
      "25201       Budget\n",
      "Name: price_range, Length: 25184, dtype: category\n",
      "Categories (4, object): ['Budget' < 'Average' < 'Expensive' < 'Extravagant']\n"
     ]
    }
   ],
   "source": [
    "print(airbnb_merged[\"price_range\"])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
