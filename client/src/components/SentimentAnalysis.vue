<template>
  <div>
    <h1>Text Sentiment Analysis</h1>
    <textarea
      id="textInput"
      name="textInput"
      rows="10"
      cols="50"
      v-model="inputData"
    ></textarea>
    <br />
    <button type="submit" class="btn" value="Submit" @click="onClick()">
      Submit
    </button>
    <br />
    <p>Results</p>
    <br />
    <vue-speedometer
      :width="300"
      :needleHeightRatio="0.7"
      :minValue="-1"
      :maxValue="1"
      :value="this.compoundData"
      :customSegmentStops="[-1, -0.25, 0.25, 1]"
      :segmentColors="['tomato', 'gold', 'limegreen']"
      currentValueText="Text Sentiment"
      :customSegmentLabels="[
        {
          text: 'Negetive',
          position: 'OUTSIDE',
          color: '#d8dee9',
        },
        {
          text: 'Neutral',
          position: 'OUTSIDE',
          color: '#d8dee9',
        },
        {
          text: 'Positive!',
          position: 'OUTSIDE',
          color: '#d8dee9',
        },
      ]"
      :ringWidth="47"
      :needleTransitionDuration="3333"
      needleTransition="easeElastic"
      needleColor="#a7ff83"
      textColor="#d8dee9"
      :height="200"
    />
    <p v-if="resultValues !== null">Compound: {{ this.compoundData }}</p>
    <p v-if="resultValues !== null">
      Neg: {{ this.resultValues.neg }} | Neu: {{ this.resultValues.neu }} | Pos:
      {{ this.resultValues.pos }}
    </p>
  </div>
</template>

<script>
import VueSpeedometer from "vue-speedometer";

export default {
  name: "SentimentAnalysis",
  components: {
    VueSpeedometer,
  },
  data() {
    return {
      inputData: "",
      compoundData: 0,
      resultValues: null,
    };
  },
  methods: {
    async onClick() {
      console.log(this.inputData);
      try {
        var data = {
          text: this.inputData,
        };
        const res = await fetch("http://127.0.0.1:5000/sentiment", {
          method: "POST",
          mode: "cors", // no-cors, *cors, same-origin
          cache: "no-cache",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
          },
          redirect: "follow",
          referrerPolicy: "no-referrer",
          body: JSON.stringify(data),
        });
        const results = await res.json();
        this.compoundData = results.compound;
        this.resultValues = results;
        console.log(results.compound);
      } catch (error) {
        console.error("Error:", error);
      }
    },
  },
};
</script>

<style scoped>
.btn {
  border: none;
  color: black;
  padding: 12px 20px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
