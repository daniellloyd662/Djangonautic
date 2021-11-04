const titleInput = document.querySelector('input[name=title]');  //grabs 'input' from the dom with the name 'title'
const slugInput = document.querySelector('input[name=slug]'); //...

// We pass in 'val' to arrow function slugify and return 'val' with a modified string suitable for a slug.
//We then add an event listener that copies the returned val into the slug on each keyup
const slugify = (val) => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-') //replace & with -and-
    .replace(/[\s\W-]+/g,'-') //replace spaces and non word chars and dashes with -
}

titleInput.addEventListener('keyup',(e) => {
  slugInput.setAttribute('value', slugify(titleInput.value))
})
