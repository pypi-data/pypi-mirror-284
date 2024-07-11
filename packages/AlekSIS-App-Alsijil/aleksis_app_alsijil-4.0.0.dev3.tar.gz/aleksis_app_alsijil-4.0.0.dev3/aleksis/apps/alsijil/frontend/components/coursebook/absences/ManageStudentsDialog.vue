<script>
import AbsenceReasonButtons from "aleksis.apps.kolego/components/AbsenceReasonButtons.vue";
import AbsenceReasonChip from "aleksis.apps.kolego/components/AbsenceReasonChip.vue";
import AbsenceReasonGroupSelect from "aleksis.apps.kolego/components/AbsenceReasonGroupSelect.vue";
import CancelButton from "aleksis.core/components/generic/buttons/CancelButton.vue";
import MobileFullscreenDialog from "aleksis.core/components/generic/dialogs/MobileFullscreenDialog.vue";
import mutateMixin from "aleksis.core/mixins/mutateMixin.js";
import documentationPartMixin from "../documentation/documentationPartMixin";
import LessonInformation from "../documentation/LessonInformation.vue";
import { updateParticipationStatuses } from "./participationStatus.graphql";
import SlideIterator from "aleksis.core/components/generic/SlideIterator.vue";
import PersonalNotes from "../personal_notes/PersonalNotes.vue";
import ExtraMarkChip from "../../extra_marks/ExtraMarkChip.vue";
import TardinessChip from "./TardinessChip.vue";
import TardinessField from "./TardinessField.vue";

export default {
  name: "ManageStudentsDialog",
  extends: MobileFullscreenDialog,
  components: {
    TardinessChip,
    ExtraMarkChip,
    AbsenceReasonChip,
    AbsenceReasonGroupSelect,
    AbsenceReasonButtons,
    PersonalNotes,
    CancelButton,
    LessonInformation,
    MobileFullscreenDialog,
    SlideIterator,
    TardinessField,
  },
  mixins: [documentationPartMixin, mutateMixin],
  data() {
    return {
      dialog: false,
      search: "",
      loadSelected: false,
      selected: [],
      isExpanded: false,
    };
  },
  props: {
    loadingIndicator: {
      type: Boolean,
      default: false,
      required: false,
    },
  },
  computed: {
    items() {
      return this.documentation.participations;
    },
  },
  methods: {
    sendToServer(participations, field, value) {
      let fieldValue;

      if (field === "absenceReason") {
        fieldValue = {
          absenceReason: value === "present" ? null : value,
        };
      } else if (field === "tardiness") {
        fieldValue = {
          tardiness: value,
        };
      } else {
        console.error(`Wrong field '${field}' for sendToServer`);
        return;
      }

      this.mutate(
        updateParticipationStatuses,
        {
          input: participations.map((participation) => ({
            id: participation.id,
            ...fieldValue,
          })),
        },
        (storedDocumentations, incomingStatuses) => {
          const documentation = storedDocumentations.find(
            (doc) => doc.id === this.documentation.id,
          );

          incomingStatuses.forEach((newStatus) => {
            const participationStatus = documentation.participations.find(
              (part) => part.id === newStatus.id,
            );
            participationStatus.absenceReason = newStatus.absenceReason;
            participationStatus.tardiness = newStatus.tardiness;
            participationStatus.isOptimistic = newStatus.isOptimistic;
          });

          return storedDocumentations;
        },
      );
    },
    handleMultipleAction(absenceReasonId) {
      this.loadSelected = true;
      this.sendToServer(this.selected, "absenceReason", absenceReasonId);
      this.$once("save", this.resetMultipleAction);
    },
    resetMultipleAction() {
      this.loadSelected = false;
      this.$set(this.selected, []);
      this.$refs.iterator.selected = [];
    },
  },
};
</script>

<template>
  <mobile-fullscreen-dialog
    scrollable
    v-bind="$attrs"
    v-on="$listeners"
    v-model="dialog"
  >
    <template #activator="activator">
      <slot name="activator" v-bind="activator" />
    </template>

    <template #title>
      <lesson-information v-bind="documentationPartProps" :compact="false" />
      <v-scroll-x-transition leave-absolute>
        <v-text-field
          v-show="!isExpanded"
          type="search"
          v-model="search"
          clearable
          rounded
          hide-details
          single-line
          prepend-inner-icon="$search"
          dense
          outlined
          :placeholder="$t('actions.search')"
          class="pt-4 full-width"
        />
      </v-scroll-x-transition>
      <v-scroll-x-transition>
        <div v-show="selected.length > 0" class="full-width mt-4">
          <absence-reason-buttons
            allow-empty
            empty-value="present"
            @input="handleMultipleAction"
          />
        </div>
      </v-scroll-x-transition>
    </template>
    <template #content>
      <slide-iterator
        ref="iterator"
        v-model="selected"
        :items="items"
        :search="search"
        :item-key-getter="
          (item) => 'documentation-' + documentation.id + '-student-' + item.id
        "
        :is-expanded.sync="isExpanded"
        :loading="loadingIndicator || loadSelected"
        :load-only-selected="loadSelected"
        :disabled="loading"
      >
        <template #listItemContent="{ item }">
          <v-list-item-title>
            {{ item.person.fullName }}
          </v-list-item-title>
          <v-list-item-subtitle
            v-if="
              item.absenceReason ||
              item.notesWithNote?.length > 0 ||
              item.notesWithExtraMark?.length > 0 ||
              item.tardiness
            "
            class="d-flex flex-wrap gap"
          >
            <absence-reason-chip
              v-if="item.absenceReason"
              small
              :absence-reason="item.absenceReason"
            />
            <v-chip
              v-for="note in item.notesWithNote"
              :key="'text-note-note-overview-' + note.id"
              small
            >
              <v-avatar left>
                <v-icon small>mdi-note-outline</v-icon>
              </v-avatar>
              <span class="text-truncate" style="max-width: 30ch">
                {{ note.note }}
              </span>
            </v-chip>
            <extra-mark-chip
              v-for="note in item.notesWithExtraMark"
              :key="'extra-mark-note-overview-' + note.id"
              :extra-mark="extraMarks.find((e) => e.id === note.extraMark.id)"
              small
            />
            <tardiness-chip
              v-if="item.tardiness"
              :tardiness="item.tardiness"
              small
            />
          </v-list-item-subtitle>
        </template>

        <template #expandedItem="{ item, close }">
          <v-card-title>
            <v-tooltip bottom>
              <template #activator="{ on, attrs }">
                <v-btn v-bind="attrs" v-on="on" icon @click="close">
                  <v-icon>$prev</v-icon>
                </v-btn>
              </template>
              <span v-t="'actions.back_to_overview'" />
            </v-tooltip>
            {{ item.person.fullName }}
          </v-card-title>
          <v-card-text>
            <absence-reason-group-select
              allow-empty
              empty-value="present"
              :loadSelectedChip="loading"
              :value="item.absenceReason?.id || 'present'"
              @input="sendToServer([item], 'absenceReason', $event)"
            />
            <tardiness-field
              v-bind="documentationPartProps"
              :loading="loading"
              :disabled="loading"
              :participation="item"
              :value="item.tardiness"
              @input="sendToServer([item], 'tardiness', $event)"
            />
          </v-card-text>
          <v-divider />
          <v-card-text>
            <personal-notes
              v-bind="documentationPartProps"
              :participation="
                documentation.participations.find((p) => p.id === item.id)
              "
            />
          </v-card-text>
        </template>
      </slide-iterator>
    </template>

    <template #actions>
      <cancel-button
        @click="dialog = false"
        i18n-key="actions.close"
        v-show="$vuetify.breakpoint.mobile"
      />
    </template>
  </mobile-fullscreen-dialog>
</template>

<style scoped></style>
