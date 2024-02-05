// Select all <a> elements with <span> having class "nchr-text"
const linksWithChapterText = Array.from(document.querySelectorAll('a span.nchr-text'))
  .filter(link => {
    const chapterNumber = parseInt(link.textContent.match(/\d+/)[0]);
    return chapterNumber > 4508;
  });

// Filter the selected elements to get only those starting with "Chapter" (case-insensitive)
const chapterLinks = linksWithChapterText
  .filter(span => span.textContent.trim().toLowerCase().startsWith('chapter'))
  .map(span => span.parentElement.href);

// Convert the array of links into a string with one link per line
const linksText = chapterLinks.join('\n');

// Create a Blob containing the text
const blob = new Blob([linksText], { type: 'text/plain' });

// Create a URL for the Blob
const blobURL = URL.createObjectURL(blob);

// Create a link element to trigger the download
const downloadLink = document.createElement('a');
downloadLink.href = blobURL;
downloadLink.download = 'chapterLinks new1.txt';
downloadLink.textContent = 'Download Chapter Links';

// Trigger the click event to start the download
downloadLink.click();
