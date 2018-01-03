<template>

    <nav class="navbar">
        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="bosstimers">Boss Timers</router-link></li>
            <li><router-link to="cooking">Cooking Calculator</router-link></li>
            <!-- <li><router-link to=""> Link </router-link></li> -->
            <li class="spacer"></li>
        </ul>
    </nav>

</template>

<script>
export default {};
</script>

<style scoped>
.navbar {
    font-family: 'Nunito Sans', sans-serif;
    overflow: auto;
    width: 100%;
    background-color: #444;
    list-style: none;
    display: block;
    clear: both;
}
.navbar ul {
    list-style: none;
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}
.navbar ul li {
    border: none;
    float: left;
    position: relative;
    border-left: 1px solid black;
    /* padding: 10px; */
    background-color: #444;
    height: 100%;
    /* width: 100%; */
}
.navbar ul li:hover {
    background-color: #555;
}
.navbar ul li:first-child {
    border: none;
}
.navbar ul li a {
    color: white;
    text-decoration: none;
    font-weight: 700;
    font-size: 1.1em;
    padding: 10px 10px;
    width: 110%;
    display: inline-block;
    /* overflow: none; */
}
.router-link-exact-active {
    background-color: #555;
}
.spacer {
    float: left;
    /* width: 100%; */
    height: 45px !important;
    width: 50%;
    border: none !important;
}
</style>
