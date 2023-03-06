# LekipMorisien
Link to figma prototype: https://www.figma.com/file/ytxBWhG0kK65tcNjffrYoV/colorcap?node-id=0%3A1&t=jjKOuKCkG1irm7yR-1

## Inspiration
Inspired by the Makercon's accurate color detection pitch, we created an accurate color detection webapp using the device camera as input.

## What it does
Color Cap allows the user to pinpoint to an object using a target displayed on the camera screen so as to accurately detect the color of the specified object. The color is output as two distinct values: an accurate name of the color and its more general and known name. A detailed description of the exact color and a text-to-speech feature are also available to the user. 

## How we built it
We first started with the front end using React Typescript. Next, we worked on the backend responsible for image processing and color detection using Python and the Color API. The front end and back end were finally connected using Flask. 

## Challenges we ran into
From the start, we discussed and brainstormed a lot about what we wanted to implement. The main challenge was connecting the front end and back end together. At first, we tried using AWS Lambda but unfortunately ran into issues importing the PIL library for Python. Consequently, we switched to Flask and also ran into issues there. The image URI contained \ and + which were reserved characters for a URL. Additionally, the URI was too long to be sent directly through the URL. This was solved by using the POST method instead. We also tried to use React Native to build a mobile app but we were running into issues when using the Expo app.

## Accomplishments that we're proud of
We are proud of the web app that we built and the challenges we successfully overcame to deliver a functional app by the deadline.

## What we learned
Teamwork and cooperation are crucial for efficiency. We learned that as long as everyone cooperates and is willing to learn, we will definitely be able to solve any challenge.

## What's next for Color Cap
Even though Color Cap is functional, there is still room for a lot of improvement. We want Color Cap to be accessible on mobile as the client described she will mainly use it outside. We also want Color Cap to describe the colors of the whole image taken through the camera instead of just a center point. Ultimately, we want Color Cap to be marketable and compete in the app market.
