<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white px-6 py-4">
			<div class="flex items-center">
				<button class="mr-3 text-gray-400 hover:text-gray-600">
					<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 19l-7-7 7-7"
						></path>
					</svg>
				</button>
				<h1 class="text-xl font-semibold text-gray-900">Create Prescription</h1>
			</div>
		</div>

		<div class="flex flex-col lg:flex-row gap-6 p-6">
			<!-- Main Content -->
			<div class="flex-1 space-y-6">
				<!-- Prescription Details Card -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<h2 class="text-lg font-medium text-gray-900 mb-4">Prescription Details</h2>
					<p class="text-sm text-gray-600 mb-6">
						Basic information about the prescription.
					</p>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Prescription Date</label
							>
							<input
								v-model="prescriptionDetails.date"
								type="date"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Prescription Type</label
							>
							<select
								v-model="prescriptionDetails.type"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select</option>
								<option value="standard">Standard</option>
								<option value="controlled">Controlled</option>
								<option value="emergency">Emergency</option>
							</select>
						</div>
					</div>

					<div class="mt-6">
						<label class="block text-sm font-medium text-gray-700 mb-2"
							>Diagnosis</label
						>
						<textarea
							v-model="prescriptionDetails.diagnosis"
							rows="3"
							placeholder="Enter diagnosis or reason for prescription"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
						></textarea>
					</div>

					<div class="mt-6">
						<label class="block text-sm font-medium text-gray-700 mb-2"
							>Pre-Medication Template</label
						>
						<div class="flex gap-3">
							<select
								class="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select template (optional)</option>
								<option value="diabetes">Diabetes Management</option>
								<option value="hypertension">Hypertension Treatment</option>
								<option value="pain">Pain Management</option>
							</select>
							<button
								class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"
							>
								Load Template
							</button>
						</div>
					</div>
				</div>

				<!-- Medication #1 -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-4">
						<h2 class="text-lg font-medium text-gray-900">Medication #1</h2>
						<button class="text-red-600 hover:text-red-700 text-sm font-medium">
							Remove
						</button>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Medication Name</label
							>
							<input
								v-model="medications[0].name"
								type="text"
								placeholder="Enter medication name"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Strength</label
							>
							<input
								v-model="medications[0].strength"
								type="text"
								placeholder="e.g., 500mg"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Dosage</label
							>
							<input
								v-model="medications[0].dosage"
								type="text"
								placeholder="e.g., 1 tablet"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Route</label
							>
							<select
								v-model="medications[0].route"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select</option>
								<option value="oral">Oral</option>
								<option value="topical">Topical</option>
								<option value="injection">Injection</option>
							</select>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Frequency</label
							>
							<select
								v-model="medications[0].frequency"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select</option>
								<option value="once-daily">Once daily</option>
								<option value="twice-daily">Twice daily</option>
								<option value="three-times">Three times daily</option>
								<option value="as-needed">As needed</option>
							</select>
						</div>
					</div>

					<div class="mt-6">
						<label class="block text-sm font-medium text-gray-700 mb-2"
							>Special Instructions</label
						>
						<textarea
							v-model="medications[0].instructions"
							rows="3"
							placeholder="Enter any special instructions for this medication"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
						></textarea>
					</div>

					<div class="flex items-center justify-between mt-6">
						<div class="flex items-center">
							<input
								v-model="medications[0].genericAllowed"
								type="checkbox"
								id="generic1"
								class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
							/>
							<label for="generic1" class="ml-2 text-sm text-gray-700"
								>Allow Generic</label
							>
						</div>
						<div class="text-sm text-gray-500">
							Number of Refills:
							<span class="font-medium">{{ medications[0].refills || 0 }}</span>
						</div>
					</div>
				</div>

				<!-- Medication #2 -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-4">
						<h2 class="text-lg font-medium text-gray-900">Medication #2</h2>
						<button class="text-red-600 hover:text-red-700 text-sm font-medium">
							Remove
						</button>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Medication Name</label
							>
							<input
								v-model="medications[1].name"
								type="text"
								placeholder="Enter medication name"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Strength</label
							>
							<input
								v-model="medications[1].strength"
								type="text"
								placeholder="e.g., 500mg"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Dosage</label
							>
							<input
								v-model="medications[1].dosage"
								type="text"
								placeholder="e.g., 1 tablet"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Route</label
							>
							<select
								v-model="medications[1].route"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select</option>
								<option value="oral">Oral</option>
								<option value="topical">Topical</option>
								<option value="injection">Injection</option>
							</select>
						</div>
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Frequency</label
							>
							<select
								v-model="medications[1].frequency"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">Select</option>
								<option value="once-daily">Once daily</option>
								<option value="twice-daily">Twice daily</option>
								<option value="three-times">Three times daily</option>
								<option value="as-needed">As needed</option>
							</select>
						</div>
					</div>

					<div class="mt-6">
						<label class="block text-sm font-medium text-gray-700 mb-2"
							>Special Instructions</label
						>
						<textarea
							v-model="medications[1].instructions"
							rows="3"
							placeholder="Enter any special instructions for this medication"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
						></textarea>
					</div>

					<div class="flex items-center justify-between mt-6">
						<div class="flex items-center">
							<input
								v-model="medications[1].genericAllowed"
								type="checkbox"
								id="generic2"
								class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
							/>
							<label for="generic2" class="ml-2 text-sm text-gray-700"
								>Allow Generic</label
							>
						</div>
						<div class="text-sm text-gray-500">
							Number of Refills:
							<span class="font-medium">{{ medications[1].refills || 0 }}</span>
						</div>
					</div>
				</div>

				<!-- Additional Information -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<h2 class="text-lg font-medium text-gray-900 mb-4">Additional Information</h2>

					<div class="mb-6">
						<label class="block text-sm font-medium text-gray-700 mb-2"
							>Notes to Pharmacist</label
						>
						<textarea
							v-model="additionalInfo.pharmacistNotes"
							rows="3"
							placeholder="Enter any additional notes for the pharmacist"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
						></textarea>
					</div>

					<div class="flex items-center">
						<input
							v-model="additionalInfo.dispenseAsWritten"
							type="checkbox"
							id="dispenseAsWritten"
							class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
						/>
						<label for="dispenseAsWritten" class="ml-2 text-sm text-gray-700"
							>Dispense as Written</label
						>
					</div>
				</div>

				<!-- Action Buttons -->
				<div class="flex flex-col sm:flex-row justify-end gap-3 pt-6">
					<button
						class="px-6 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
					>
						Cancel
					</button>
					<button
						class="px-6 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"
					>
						Create Prescription
					</button>
				</div>
			</div>

			<!-- Right Sidebar -->
			<div class="w-full lg:w-80 space-y-6">
				<!-- Patient Information -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<h3 class="text-lg font-medium text-gray-900 mb-4">Patient Information</h3>
					<p class="text-sm text-gray-600 mb-4">
						Current patient for this prescription.
					</p>

					<div class="flex items-center mb-4">
						<div
							class="h-12 w-12 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white font-semibold"
						>
							JS
						</div>
						<div class="ml-3">
							<div class="text-sm font-medium text-gray-900">John Smith</div>
							<div class="text-xs text-gray-500">DOB: Feb 15, 1985</div>
						</div>
					</div>

					<div class="space-y-2 text-sm">
						<div>
							<span class="text-gray-500">Allergies:</span>
							<span class="ml-2 text-gray-900">Penicillin</span>
						</div>
						<div>
							<span class="text-gray-500">Conditions:</span>
							<span class="ml-2 text-gray-900">Diabetes, Hypertension</span>
						</div>
					</div>

					<button
						class="w-full mt-4 text-sm text-blue-600 hover:text-blue-700 font-medium"
					>
						View patient details
					</button>
				</div>

				<!-- Prescription History -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-lg font-medium text-gray-900">Prescription History</h3>
						<button class="text-sm text-blue-600 hover:text-blue-700 font-medium">
							View All Prescriptions
						</button>
					</div>

					<div class="space-y-4">
						<div class="flex justify-between items-start">
							<div>
								<div class="text-sm font-medium text-gray-900">
									Lisinopril 10mg
								</div>
								<div class="text-xs text-gray-500">Prescribed: June 15, 2023</div>
							</div>
							<div class="text-xs text-gray-500">0</div>
						</div>

						<div class="flex justify-between items-start">
							<div>
								<div class="text-sm font-medium text-gray-900">
									Metformin 500mg
								</div>
								<div class="text-xs text-gray-500">Prescribed: May 20, 2023</div>
							</div>
							<div class="text-xs text-gray-500">2</div>
						</div>

						<div class="flex justify-between items-start">
							<div>
								<div class="text-sm font-medium text-gray-900">
									Amoxicillin 250mg
								</div>
								<div class="text-xs text-gray-500">Prescribed: April 10, 2023</div>
							</div>
							<div class="text-xs text-gray-500">0</div>
						</div>
					</div>
				</div>

				<!-- Prescription Options -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
					<h3 class="text-lg font-medium text-gray-900 mb-4">Prescription Options</h3>

					<div class="space-y-4">
						<div>
							<label class="block text-sm font-medium text-gray-700 mb-2"
								>Prescription Priority</label
							>
							<select
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
							>
								<option value="standard">Standard</option>
								<option value="urgent">Urgent</option>
								<option value="routine">Routine</option>
							</select>
						</div>

						<div class="space-y-3">
							<div class="flex items-center">
								<input
									type="checkbox"
									id="emailPatient"
									class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
								/>
								<label for="emailPatient" class="ml-2 text-sm text-gray-700"
									>Email Patient Instructions</label
								>
							</div>

							<div class="flex items-center">
								<input
									type="checkbox"
									id="textReminder"
									class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
								/>
								<label for="textReminder" class="ml-2 text-sm text-gray-700"
									>Text Reminders Schedule</label
								>
							</div>

							<div class="flex items-center">
								<input
									type="checkbox"
									id="pharmacyNotify"
									class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
								/>
								<label for="pharmacyNotify" class="ml-2 text-sm text-gray-700"
									>Notify Preferred Pharmacy</label
								>
							</div>
						</div>

						<div class="pt-3 border-t border-gray-200">
							<div class="flex items-center">
								<input
									type="checkbox"
									id="sendToPatient"
									class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
								/>
								<label for="sendToPatient" class="ml-2 text-sm text-gray-700"
									>Send to Patient</label
								>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

// Prescription details
const prescriptionDetails = ref({
	date: '',
	type: '',
	diagnosis: '',
})

// Medications array
const medications = ref([
	{
		name: '',
		strength: '',
		dosage: '',
		route: '',
		frequency: '',
		instructions: '',
		genericAllowed: false,
		refills: 0,
	},
	{
		name: '',
		strength: '',
		dosage: '',
		route: '',
		frequency: '',
		instructions: '',
		genericAllowed: false,
		refills: 0,
	},
])

// Additional information
const additionalInfo = ref({
	pharmacistNotes: '',
	dispenseAsWritten: false,
})

// Methods for form handling
const addMedication = () => {
	medications.value.push({
		name: '',
		strength: '',
		dosage: '',
		route: '',
		frequency: '',
		instructions: '',
		genericAllowed: false,
		refills: 0,
	})
}

const removeMedication = (index) => {
	if (medications.value.length > 1) {
		medications.value.splice(index, 1)
	}
}

const createPrescription = () => {
	// Handle form submission
	console.log('Creating prescription...', {
		prescriptionDetails: prescriptionDetails.value,
		medications: medications.value,
		additionalInfo: additionalInfo.value,
	})
}
</script>
