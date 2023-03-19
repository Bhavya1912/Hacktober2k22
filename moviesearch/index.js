<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MOVIE SEARCH</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <!-- header part -->
  <div class="header">
    <div class="heading" align="center">MOVIE DB</div>
    <div class="search">
      <input type="text" placeholder="Search" class="input">
    </div>
    <div class="search">
    <button type="submit" class="input" onclick="find()">Submit</button>
    </div>
  </div>

  <!-- end of header part -->

  <!-- main body div part -->
  <div class="main">

  </div>

  <!-- end of main body -->
</body>
<script>
  const API = "api_key=b34fb3572a141f45dd05b783f7d565be";
  const BASEURL = "https://api.themoviedb.org/3";
  const APIURL = BASEURL + '/discover/movie?sort_by=popularity.desc&' + API;
  const IMGURL = "https://image.tmdb.org/t/p/w500";
  const main = document.querySelector(".main");
  const form = document.querySelector(".search");
  const input = document.querySelector(".input");
  const SEARCHURL = BASEURL + '/search/movie?' + API;

  // functions
  getMovies(APIURL);

  function getMovies(url) {
    fetch(url).then(data =>
      data.json()).then((res) => {
        console.log(res);
        showMovies(res.results);
      })
  }

  function showMovies(res) {
main.innerHTML="";
    res.forEach((movie) => {
      const { title, poster_path, vote_average, overview } = movie;
      const movieEl = document.createElement('div');
      movieEl.classList.add('super');
      movieEl.innerHTML = `<div class="indivisual" id="ind1">
            <div class="movImage">
              <img src="${IMGURL + poster_path}" alt="${title}" class="image">
            </div>
            <div class="reg">
              <div class="title">
              ${title}
              </div>
              <div class="rating">
               ${vote_average}
              </div>
            </div>
            <div class="info">
       ${overview}
            </div>
          </div>`


      main.appendChild(movieEl);
    })
  }

  function find(){

    const select = input.value;
      getMovies(SEARCHURL + '&query=' + select);
      input.value="";
  }

</script>


</html>