
const requests = {
   fetchTrending: '/trending/all/week?api_key=0462b527b038329d06060fda6bf7b04b&language=en-US',
   fetchNetflixOriginals: '/discover/tv?api_key=0462b527b038329d06060fda6bf7b04b&with_networks=213',
   fetchTopRated:'/movie/top_rated?api_key=0462b527b038329d06060fda6bf7b04b&language=en-US',
   fetchActionMovies:'/discover/movie?api_key=0462b527b038329d06060fda6bf7b04b&with_genres=28',
  fetchComedyMovies: '/discover/movie?api_key=0462b527b038329d06060fda6bf7b04b&with_genres=35',
  fetchHorrorMovies:'/discover/movie?api_key=0462b527b038329d06060fda6bf7b04b&with_genres=27',
  fetchRomanceMovies:'/discover/movie?api_key=0462b527b038329d06060fda6bf7b04b&with_genres=10749',
  fetchDocumentaries: '/discover/movie?api_key=0462b527b038329d06060fda6bf7b04b&with_genres=99',
}

export default requests;
