<template>
  <v-app>
    <v-app-bar
      app
      color="black"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          class="head1"
          contain
          src="https://cdn.freebiesupply.com/images/large/2x/nintendo-logo-black-and-white.png"
          transition="scale-transition"
        />
      </div>
<!-- 
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer> -->

      <div>
        <v-img
          class="head2"
          contain
          src="https://i.imgur.com/qRQg7MB.jpg"
          transition="scale-transition"
        />
      </div>

      <!-- <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer> -->

      <div class="d-flex align-center">
        <v-img
          class="head3"
          contain
          src="https://vignette.wikia.nocookie.net/projectxzone/images/e/e0/Monolith_Soft.png/revision/latest?cb=20160605093011"
          transition="scale-transition"
        />
      </div>
    </v-app-bar>

    <v-content>
      <CoreCrystal/>
    </v-content>
  </v-app>
</template>

<script>
import CoreCrystal from './components/CoreCrystal';

export default {
  name: 'App',

  components: {
    CoreCrystal,
  },

  data: () => ({
    //
  }),
};
</script>
