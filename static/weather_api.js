/* Apparently I can't use 'location' and have to use city because else 
I get "Uncaught SyntaxError: Identifier 'location' has already been declared". 
I haven't used 'location' anywhere else in my file...Ok, after avoiding this error, 
I found out that the JSON response already has "location" in it. I guess that's why. 
But I couldn't know, at least not with the docs... */


let currentType = "current.json";
let userCity = "London";

let apiData = {
    url: "http://api.weatherapi.com/v1",
    type: `${currentType}`,
    key: "40cd513af8aa446484a92837213011",
    city: `${userCity}`,
  };


let { url, type, key, city } = apiData;

let apiUrl = `${url}/${type}?key=${key}&q=${city}`;

console.log("apiUrl:");
console.log(apiUrl);

 fetch(apiUrl)
   .then((data) => {
     if (data.ok) {
       return data.json();
     }
     throw new Error("Response not ok.");
   })
   .then((locationRequest) => generateHtml(locationRequest))
   .catch((error) => console.error("Error:", error));

 const generateHtml = (data) => {
   console.log("data:")
   console.log(data);
   console.log("data.location.name:")
   console.log(`${data.location.name}`);
   const html = `
   <div class="location-and-details">
     <div class="weather-location">
        <h1>${data.location.name}, ${data.location.country}</h1></div>
     <div class="details">
         <span>Tmp: ${data.current.temp_c} °C</span>
         <span>Feels like: ${data.current.feelslike_c} °C</span>
     </div>
     </div>
 `;
   const weatherDiv = document.querySelector(".weather");
   weatherDiv.innerHTML = html;
};
/* SEARCH BAR */

const citiesList = document.getElementById('weather-cities');
const searchBar = document.getElementById('weather-searchbar');
let cities = [];

console.log("citiesList:");
console.log(citiesList);
console.log("searchBar:");
console.log(searchBar);

searchBar.addEventListener('keyup', (e) => {
    userCity = e.target.value.toLowerCase();
    console.log("usercity:");
    console.log(userCity);
    const filteredCities = cities.filter((city) => {
        console.log(city.name.toLowerCase().includes(userCity));
        return (
            city.name.toLowerCase().includes(userCity) ||
            city.region.toLowerCase().includes(userCity) ||
            city.country.toLowerCase().includes(userCity)
        );
    });
    console.log("filteredCities:");
    console.log(filteredCities);
    displayCities(filteredCities);
});

const loadCities = async () => {
    try {
        currentType = "search.json";
        apiUrl = `${url}/${currentType}?key=${key}&q=${userCity}`; /* I added this line bc before the currentType assignment 1 line above didn't affect any change"*/
        console.log("new apiUrl:")
        console.log(apiUrl)
        const res = await fetch(apiUrl);
        cities = await res.json();
        console.log("cities:");
        console.log(cities);
        // displayCities(cities);
    } catch (err) {
        console.error(err);
    }
};

const displayCities = (cities) => {
    let htmlString = cities
        .map((city) => {
            return `
            <li class="city-list px-4 py-1 my-2 mx-1">
                <p>${city.name}</p>
            </li>
        `;
        })
        .join('');
    citiesList.innerHTML = htmlString;
};

// const optionsCities = document.querySelector(".city-list");

// optionsCities.addEventListener("click", () => {
//     currentType = "current.json";
//     const selectedCity = document.querySelector(".city-list");
//     userCity = selectedCity.innerHTML;
//     apiUrl = `${url}/${currentType}?key=${key}&q=${userCity}`;
//     fetch(apiUrl);
// })



loadCities();