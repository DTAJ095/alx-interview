#!/usr/bin/node
/**
 * Wrapper function for the Star Wars API that
 * allows it to work with async/await.
 * @param {string} url - The URL to make the request to.
 * @returns {Promise} - The promise object representing the request.
 */
function makeRequest(url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body));
    });
  });
}

/**
 * Entry point - makes a request to the Star Wars API
 * and prints the names of the characters in the response.
 * in order of appearance in the films.
 */
async function main() {
    const args = process.argv;

    if (args.length !== 3) {
        console.log('Usage: ./0-starwars_characters.js <film number>');
        process.exit(1);
    }

    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
    const movie = await makeRequest(movieUrl);

    if (movie.characters == undefined) {
        console.log('No characters found');
        process.exit(1);
    }

    for (const characterUrl of movie.characters) {
        const character = await makeRequest(characterUrl);
        console.log(character.name);
    }
}

main();