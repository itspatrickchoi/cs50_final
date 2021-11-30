/* For whatever reason I can't use 'location' and have to use city because else I get "Uncaught SyntaxError: Identifier 'location' has already been declared". I haven't used 'location' anywhere else in my file...someone enlighten me pls */
const apiData = {
    url: "http://api.weatherapi.com/v1",
    type: "current.json",
    key: "40cd513af8aa446484a92837213011",
    city: "London",
  };

const { url, type, key, city } = apiData;

const apiUrl = `${url}/${type}?key=${key}&q=${city}`;

console.log(apiUrl);


fetch(apiUrl)
    .then( (data) => {
        if(data.ok){
            return data.json()
        }
        throw new Error('Response not ok.'); 
    })
    .then( location => generateHtml(location))
    .catch( error => console.error('Error:', error))


const generateHtml = (data) => {
    console.log(data)
    const html = `
        <div class="name">${data.name}</div>
        <img src=${data.sprites.front_default}>
        <div class="details">
            <span>Height: ${data.height}</span>
            <span>Weight: ${data.weight}</span>
        </div>
    `
    const pokemonDiv = document.querySelector('.pokemon')
    pokemonDiv.innerHTML = html}