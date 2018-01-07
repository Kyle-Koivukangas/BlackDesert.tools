<template>
<div>
    <h3>work in progress below.. <br> (prices are just rough averages, input your own for more accurate results)</h3>
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
                    <option v-for="i in range(0, 11)" :value="'Beginner ' + i">Beginner {{ i }}</option>
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
                                <h3>Ingredients:</h3>
                <ul>
                    <li v-for="ingredient in ingredients">{{ ingredient }}: {{ recipes[selectedRecipe][ingredient] }}</li>
                </ul>
                <!-- <p>Raw Data:{{ getKeys(recipes[selectedRecipe]) }}</p> -->
                <!-- {{ selectedRecipe }} -->
            </div>

            <!-- <div class="ingredients">
                <h3>Ingredients:</h3>
                <ul>
                    <li v-for="ingredient in ingredients">{{ ingredient }}: {{ recipes[selectedRecipe][ingredient] }}</li>
                </ul>
            </div> -->

            <div class="bulk-calc">
                <h2>Batch Calculator:</h2>
                <label for="amount">Amount to make:</label>
                <input type="number" id="amount" name="amount" value="100" v-model="amount"> 
                <br> <br>
                <div class="req-ingredients">
                    Required Ingredients to make {{ amount }} recipes:
                    <ul>
                        <li v-for="ingredient in ingredients">
                            {{ recipes[selectedRecipe][ingredient] * amount }} {{ ingredient }}
                            <input class="ing-price-input" type="number" :id="ingredient" v-model="ingPrices[ingredients.indexOf(ingredient)]">
                            <label style="text-align:right;" :for="ingredient">price per:</label>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="results">
                <strong>Results:</strong>
                <br>
                {{ amount }} batches of {{ selectedRecipe }} at Cooking {{ cookingLevel }} will yield: <br> <br>
                {{ quantityProduced }} {{ selectedRecipe }} 
                (with {{ amount * (skillMultiplier/10) }} rare procs) <br>
                <br>
                {{ selectedRecipe }} sells for: <input type="number" id="" v-model="productPrice">/piece <br>
                Cost per item: {{ costPerItem }} <br>
                Profit per item: {{ productPrice-costPerItem }} <br>
                Profit for batch: {{ (productPrice-costPerItem)*amount }}
            

                <!-- <br>
                Not finished yet, yield isn't yet calculated.. <br>
                This will calculate the yield based on cooking level, eventually. -->
            </div>

        </div>
    </div>

</div>
</template>

<script>
import Recipes from "../../assets/recipes.json";
import PriceBank from "../../assets/priceBank.json";

export default {
    data() {
        return {
            recipes: Recipes,
            priceBank: PriceBank,
            selectedRecipe: "White Sauce",
            cookingLevel: "Professional 1",
            amount: 1000,
            ingPrices: {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
            },
            productPrice: 0
        };
    },
    computed: {
        ingredients() {
            return this.getKeys(this.recipes[this.selectedRecipe]).splice(1);
        },
        skillMultiplier() {
            var level = this.cookingLevel.split(' ')[0]
            if (level === 'Master') {
                return 3.5
            } else if (level === 'Artisan'){
                return 3
            } else if (level === 'Professional') {
                return 2.5
            } else if (level === 'Skilled') {
                return 2
            } else {
                return 1.5
            }
        },
        quantityProduced() {
            return this.amount * this.skillMultiplier
        },
        costPerItem() {
            var recipeCost = 0;
            for (var i = 0; i < Object.keys(this.ingPrices).length; i++) {
                recipeCost += this.ingPrices[i]
            }
            return (recipeCost * this.amount)/this.quantityProduced
        }
    },
    watch: {
        selectedRecipe() {
            var prices = [];
            for (var i = 0; i < this.ingredients.length; i++) {
                var mean = (Number(this.priceBank[this.ingredients[i]].high) + Number(this.priceBank[this.ingredients[i]].low)) / 2;
                // console.log(`item: ${this.ingredients[i]} \nmean: ${mean}`);
                prices.push(mean);
                this.ingPrices[i] = mean;
            }
            this.productPrice = this.priceBank[this.selectedRecipe].high
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
ul {
    line-height: 1.4em;
}
label {
    width: 250px;
}
input {
    width: 55px;
}
.ing-price-input {
    float: right;
    margin-right: 10em;
}
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
    text-align: left;
    grid-row-start: 1;
    grid-row-end: 3;
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
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 3;
    background-color: rgb(192, 192, 192);
}
.req-ingredients {
    text-align: left;
}
.results {
    text-align: left;
    grid-column-start: 1;
    grid-column-end: 3;
    background-color: rgb(207, 207, 207);
}
</style>
