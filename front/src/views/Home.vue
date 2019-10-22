<template>
  <div class="home">
    <ApartmentsSearch />
  </div>
</template>

<script>
// @ is an alias to /src
import ApartmentsSearch from '@/components/ApartmentsSearch.vue';


export default {
  name: 'home',
  components: {
    ApartmentsSearch,
  },
};
</script>
