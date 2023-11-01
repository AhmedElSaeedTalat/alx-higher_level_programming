$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, textStatus) {
  const name = data.name;
  $('DIV#character').text(name);
});
