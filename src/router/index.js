import Vue from "vue";
import Router from "vue-router";

import Home from "@/components/Home";
import BossTimers from "@/components/bossTimers/BossTimers";
import CookingCalc from "@/components/cookingCalculator/CookingCalc";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
        },
        {
            path: "/bosstimers",
            name: "BossTimers",
            component: BossTimers,
        },
        {
            path: "/cooking",
            name: "CookingCalc",
            component: CookingCalc,
        },
    ],
});
