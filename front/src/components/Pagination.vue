<template>
  <div class="custom-pagination">
    <ul>
      <li style="display: inline;"
        v-for="page in pages" v-bind:key="page">
        <button @click="getPage(page)">{{ page }} страница</button>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'Pagination',
  props: ['pages', 'getPage'],
};
</script>
