<template>
<div class="batch-calc">
    <h2>Batch Calculator:</h2>
    <label for="amount">Amount to make:</label>
    <input type="number" id="amount" name="amount" value="100" v-model="amount"> 
    <br> <br>
    <div class="req-ingredients">
        Required Ingredients to make {{ amount }} recipes:
        <ul>
            <li v-for="ingredient in ingredients">
                {{ recipes[selectedRecipe][ingredient] * amount }} {{ ingredient }}
                @<input type="number" id="">/piece
            </li>
        </ul>
    </div>

    <div class="results">
        <strong>Resulting yield:</strong>
        <br>
        Not finished yet, yield isn't yet calculated.. <br>
        This will calculate the yield based on cooking level, eventually.
    </div>
</div>
  
</template>

<script>
export default {
    props: {
        recipe: Object,
        default: function() {
            return {
                
            }
        }
    },

};
</script>

<style scoped>


</style>
