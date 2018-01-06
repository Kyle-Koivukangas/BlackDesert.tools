<template>
<div>
    <div class="title-box">
        <h1>Cooking Calculator</h1>
    </div>    
    <div class="temp-construction">
        <img src="../../assets/CookingUtensil.png" alt="">
        <h3>I'm not done yet, go away!</h3>
    </div>

    <vue-cooking-calc></vue-cooking-calc>

</div>
  
</template>

<script>
import VueCookingCalc from "./CookingCalc.vue";

export default {
    components: {
        VueCookingCalc,
    },
    data() {
        return {};
    },
};
</script>

<style scoped>
img {
    height: 500px;
    width: 500px;
}

</style>
