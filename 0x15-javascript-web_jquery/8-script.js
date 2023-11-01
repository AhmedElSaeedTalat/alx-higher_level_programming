$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const results = data.results;
  for (let i = 0; i < results.length; i++) {
    $('UL#list_movies').append(`<li>${results[i].title}</li>`);
  }
});
