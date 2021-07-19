import streamlit as st

st.set_page_config(page_title='Crime in Chicago')

st.write("""
### Chicago Crime Report
""")

st.write("""
**Crime in Chicago** has been tracked by the **Chicago Police Department's Bureau of Records** since the beginning of the 20th centuty.
The city's overall crime rate, especially the violent crime rate, is substantially higher that the US average.
""")

st.write("""
In this project, I am going to explore more about crime in Chicago and try to answer few questions:

*1. How has crime in Chicago changed accross years?*

*2. Is the crime rate is corralated with the arrest rate in the city?*

*3. Are some types of crimes more likely to happen in specific locations or specific time?*
""")



st.write("""
## Let us begin!
""")

st.write("""
On this chart we can see a clear periodic pattern in the crimes over many years.
""")

st.image('chicago_crimes/img/crimes_per_month.png', width=695)

st.write("""
Now let's take a look on the arrest rate during the same period of time.
""")

st.image('chicago_crimes/img/arrests.png', width=695)

st.write("""
As we can see both of the charts have a similar downtrand, that means crimes and arrest are corralated with each other.
I think we already have an answer for questions #1 and #2.
""")

st.write("""
Now let's separate crimes by type and see is there any difference?
""")
st.image('chicago_crimes/img/crime_type.png', width=695)
st.write("""
*Credit for this plot goes to:* **Fahd Alhazmi**
""")
st.write("""
Here we can see that some types of crimes are in downtrand and these are: **Assaults, Battery, Burglary, Damage, Criminal Trespass, Gambling, Kidnapping, Narcotics, Vehicle Theft, Prostitution, Robbery and Theft** that means that Chicago Police Department is doing a great job to prevent these crimes.
""")

st.write("""
On the other side, we can see that there are still crimes that are having a strong uptrand. **Sexual Assaults, Deceptive Practices, Homicides, Human Trafficking, Obscenity, Stalking and Weapons Violations**.
""")

st.write("""
There is a lot of work that should be done to prevent all this crimes. I would like to hear your thoughs on how we, as a community can change the situation for our city?
""")


st.write("""
On this chart we are going to look at crime distribution by type.
""")
st.image('chicago_crimes/img/crimes_by_type2.png', width=695)
st.write("""
We can see that some types of crime are most common to happen in Chicago area. The top 5 crimes from 2001 - Present are **Theft**,**Battery**, **Criminal Damage**, **Narcotics** and **Assaults**.
""")


st.write("""
Now let's take a look at the similiar distribution of crime but now by location.
""")
st.image('chicago_crimes/img/2crimes_by_location.png', width=695)
st.write("""
This chart is providing very important information for us as residents of Chicago City. From here we can see that most of the crimes are use to happen on the streets **1.909.913** cases as well as **706.919** cases on Sidewalk.
Residences and Appartments are on the top of the list too and I believe it has too deal with specific type or crime that happens in these locations.
""")

st.write("""
This dataset is imported from [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g). Cointains a record of crimes occured in the City of Chicago from 2001 to present, minus the most recent seven days.
""")
