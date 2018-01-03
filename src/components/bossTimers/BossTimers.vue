<template>
    <div>
        <!-- <p>Errors: {{ errors }}</p> -->
        <div class="title-container">
            <h1>Boss Timers</h1>
        </div>

        <vue-boss-times></vue-boss-times>

    </div>
</template>

<script>

import vueBossTimes from './BossTimes.vue';

export default {
    components: {
        vueBossTimes,
    },
    data() {
        return {};
    },
};
</script>

<style>
.title-container {
    width: calc(80% + 10px);
    margin: auto;
    display: flex;
    justify-content: center;
    /* border-radius: 3px; */
    /* justify-content: center; */
    color: rgb(63, 67, 78);
    font-family: 'Alegreya Sans', sans-serif;
}

</style>
