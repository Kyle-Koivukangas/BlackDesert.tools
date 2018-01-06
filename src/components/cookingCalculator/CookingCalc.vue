<template>
<div>
    <h3>work in progress below..</h3>
    <div class="calc-window">
        <!-- <h1>{{ selectedRecipe }}</h1> -->
        <div class="recipe-selection">
            <label for="recipes">Select a recipe:</label>
            <select name="recipes" id="recipe" v-model="selectedRecipe">
                <option v-for="recipe in Object.keys(recipes)" :value="recipe">{{ recipe }}</option>
            </select>
            <label for="level">Cooking Level:</label>
            <select name="level" id="level" v-model="cookingLevel">
                <optgroup label="Beginner">
                    <option v-for="i in range(0, 11)" :value="'beginner ' + i">Beginner {{ i }}</option>
                </optgroup>
                <optgroup label="Apprentice">
                    <option v-for="i in range(0, 11)" :value="'Apprentice ' + i">Apprentice {{ i }}</option>
                </optgroup>
                <optgroup label="Skilled">
                    <option v-for="i in range(0, 11)" :value="'Skilled ' + i">Skilled {{ i }}</option>
                </optgroup>
                <optgroup label="Professional">
                    <option v-for="i in range(0, 11)" :value="'Professional ' + i">Professional {{ i }}</option>
                </optgroup>
                <optgroup label="Artisan">
                    <option v-for="i in range(0, 11)" :value="'Artisan ' + i">Artisan {{ i }}</option>
                </optgroup>
                <optgroup label="Master">
                    <option v-for="i in range(0, 30)" :value="'Master ' + i">Master {{ i }}</option>
                </optgroup>
            </select>
        </div>

        <div v-if="selectedRecipe" class="grid">
            <div class="recipe-info">
                <h3>{{ selectedRecipe }}</h3>
                <p v-if="selectedRecipe">Level Requirement: {{ recipes[selectedRecipe]['levelReq'] }}</p>
                <br>
                <!-- <p>Raw Data:{{ getKeys(recipes[selectedRecipe]) }}</p> -->
                <!-- {{ selectedRecipe }} -->
            </div>

            <div class="ingredients">
                <!-- {{ selectedRecipe }} -->
                <h3>Ingredients:</h3>
                <ul>
                    <li v-for="ingredient in ingredients">{{ ingredient }}: {{ recipes[selectedRecipe][ingredient] }}</li>
                </ul>
            </div>

            <div class="bulk-calc">
                <label for="amount">Amount to make:</label>
                <input type="number" id="amount" name="amount" value="100" v-model="amount">
                <div class="req-ingredients">
                    Required Ingredients to make {{ amount }} recipes:
                    <ul>
                        <li v-for="ingredient in ingredients">{{ ingredient }}: {{ recipes[selectedRecipe][ingredient] * amount }}</li>
                    </ul>
                </div>

                <div class="results">
                    <strong>Resulting yield:</strong>
                    <br>
                    Not finished yet, yield isn't yet calculated.. <br>
                    This will calculate the yield based on cooking level, eventually.
                </div>
            </div>

        </div>
    </div>

</div>
</template>

<script>
import Recipes from "../../assets/recipes.json";

export default {
    data() {
        return {
            recipes: Recipes,
            selectedRecipe: "Beer",
            cookingLevel: 'Professional 1',
            amount: 100,
        };
    },
    computed: {
        ingredients() {
            return this.getKeys(this.recipes[this.selectedRecipe]).splice(1);
        },
    },
    methods: {
        getKeys(obj, keys) {
            keys = keys || [];
            for (var key in obj) {
                keys.push(key);
                if (obj[key] instanceof Object) keys.concat(getKeys(obj[key], keys));
            }

            return keys.filter(function(elem, pos, self) {
                return self.indexOf(elem) == pos;
            });
        },
        range(start, count) {
            return Array.apply(0, Array(count)).map(function(element, index) {
                return index + start;
            });
        },
    },
};
</script>

<style scoped>
.calc-window {
    background-color: #777;
}
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
}
.recipe-info {
    grid-column: 1;
    background-color: #888;
}
.ingredients {
    grid-column: 2;
    text-align: left;
    background-color: #999;
}
.ingredients ul {
    text-align: left;
    margin: auto;
    margin-left: 20%;
}
.bulk-calc {
    grid-column-start: 1;
    grid-column-end: 3;
    background-color: rgb(192, 192, 192);
}
.req-ingredients {
    text-align: left;
}
.results {
    text-align: left;
}
</style>
