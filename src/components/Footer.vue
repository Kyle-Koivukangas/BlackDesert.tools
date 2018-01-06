<template>
  <div class="footer">
    <div class="section" v-for="i in [1,2,3,4]">footer section {{ i }}</div>

  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.footer {
    margin-top: 25px;
    padding : 20px;
    clear: both;
    display: block;
    background-color: #444;
    color: #999;
    display: flex;
    justify-content: space-around;
    align-items: center;
    bottom: 0px;
    height: 100px;
}
.section {
    padding: 10px 2.4rem;
    border-left: 1px solid #222;
}
.section:first-child {
    border: none;
}

</style>
