<template>
    <div id="app">
        <!-- <img src="./assets/logo.png"> -->
        <div class="wrapper">
            
            <div class="header">
                <div class="title">
                    <h1 style="margin: 10px 0">Black Desert Tools</h1>
                    <!-- <hr class="marginfix"> -->
                    <div class="hr"></div>
                    <p style="margin: 10px 0">Your source for Blackuhh Deserterruh Tuulsuh!</p>
                </div>

                <vue-nav-bar></vue-nav-bar>
            </div>

            <router-view/>

            <vue-footer></vue-footer>

        </div>
    </div>
</template>

<script>
import VueNavBar from "./components/NavBar.vue";
import VueFooter from "./components/Footer.vue";

export default {
    name: "app",
    components: {
        VueNavBar,
        VueFooter,
    }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Alegreya+Sans|Eczar|Nunito+Sans|Proza+Libre');
/* Fonts:
font-family: 'Alegreya Sans', sans-serif;
font-family: 'Nunito Sans', sans-serif;
font-family: 'Eczar', serif;
font-family: 'Proza Libre', sans-serif; */

body {
    color: white;
    background-color: #505255;
    font-family: 'Nunito Sans', sans-serif;
}
#app {
    margin-top: 50px;
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /* margin-top: 60px; */
}

.wrapper {
    margin: 50px auto;
    width: 980px;
    background-color: white;
    box-shadow: 0 0 12px black;
}
.header {
    width: 100%;
    height: 180px;
    text-align: left;
    background-image: url("./assets/bdoLandscapeBanner.jpg");
    background-position-y: -65px;
    color: white;
    text-shadow: 0 0 10px black;
}
.title {
    margin: 40px 0 0px 45px;
    height: 100px; 
    display: inline-block; 
    font-family: 'Alegreya Sans', sans-serif;
}
.title h1 {
    margin: 0px!important;
    font-family: 'Eczar', serif;
    font-size: 2.2em;
}
.title p {
    font-size: 1.1em;
}
.hr {
    height: 1px;
    width: 18rem;
    background-color: #777;
    box-shadow: 0 1px 1px #444;
    border-radius: 500px;
    margin-top: -15px;
}
.marginfix {
    margin: 0;
}
vue-nav-bar {
    bottom: 0px;
}

@media screen and (min-width: 1000px) {
    .wrapper {
        margin: auto;
        width: 980px;
    }
}
@media screen and (min-width: 1920px) {
    .wrapper {
        margin: auto;
        width: 1280px;
    }
}
@media screen and (max-width: 600px) {
    body {
        padding: 0;
        margin: 0;
    }
    .wrapper {
        margin: 0;
        width: 100%;
    }
}
</style>
