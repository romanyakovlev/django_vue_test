<template>
  <div class="custom-checkbox">
    <input type="checkbox" @click="clicked">
    {{toggle}}
  </div>
</template>

<script>
export default {
  name: 'Checkbox',
  props: ['toggle'],
  methods: {
    clicked() {
      this.$emit('update:toggle', !this.toggle);
      this.$emit('requestApi');
    },
  },
};
</script>

<style>

</style>
