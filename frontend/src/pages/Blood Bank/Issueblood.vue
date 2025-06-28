<template>
	<div class="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
		<div class="">
			<!-- Header -->
			<div class="mb-8">
				<h1 class="text-3xl font-bold text-gray-900 mb-2">Issue Blood</h1>
				<p class="text-gray-600">
					Complete the form below to issue blood to a patient or external recipient.
				</p>
			</div>

			<!-- Form Container -->
			<div class="bg-white shadow-lg rounded-lg overflow-hidden">
				<div class="px-6 py-8">
					<h2 class="text-xl font-semibold text-gray-900 mb-6">Blood Issue Form</h2>
					<p class="text-sm text-gray-600 mb-8">
						Fill out all required information to issue blood units.
					</p>

					<form @submit.prevent="handleSubmit" class="space-y-8">
						<!-- Recipient Information -->
						<div>
							<h3 class="text-lg font-medium text-gray-900 mb-4">
								Recipient Information
							</h3>

							<!-- Recipient Type -->
							<div class="mb-6">
								<label class="block text-sm font-medium text-gray-700 mb-3"
									>Recipient Type</label
								>
								<div class="flex space-x-4">
									<button
										type="button"
										@click="recipientType = 'hospital'"
										:class="[
											'px-4 py-2 text-sm font-medium rounded-sm transition-colors',
											recipientType === 'hospital'
												? 'bg-gray-900 text-white'
												: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
										]"
									>
										Hospital Patient
									</button>
									<button
										type="button"
										@click="recipientType = 'external'"
										:class="[
											'px-4 py-2 text-sm font-medium rounded-sm transition-colors',
											recipientType === 'external'
												? 'bg-gray-900 text-white'
												: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
										]"
									>
										External Recipient
									</button>
								</div>
							</div>

							<!-- Patient Selection -->
							<div class="mb-6">
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Patient</label
								>
								<select
									v-model="selectedPatient"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
								>
									<option value="">Select patient</option>
									<option value="patient1">John Doe - ID: 12345</option>
									<option value="patient2">Jane Smith - ID: 67890</option>
									<option value="patient3">Michael Johnson - ID: 11111</option>
								</select>
							</div>
						</div>

						<!-- Blood Information -->
						<div>
							<h3 class="text-lg font-medium text-gray-900 mb-4">
								Blood Information
							</h3>

							<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
								<!-- Blood Type -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Blood Type</label
									>
									<select
										v-model="bloodType"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">Select blood type</option>
										<option value="A+">A+</option>
										<option value="A-">A-</option>
										<option value="B+">B+</option>
										<option value="B-">B-</option>
										<option value="AB+">AB+</option>
										<option value="AB-">AB-</option>
										<option value="O+">O+</option>
										<option value="O-">O-</option>
									</select>
								</div>

								<!-- Number of Units -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Number of Units</label
									>
									<input
										type="number"
										v-model="numberOfUnits"
										min="1"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										placeholder="1"
									/>
									<p class="text-xs text-gray-500 mt-1">
										Each unit is approximately 450ml
									</p>
								</div>
							</div>
						</div>

						<!-- Issue Details -->
						<div>
							<h3 class="text-lg font-medium text-gray-900 mb-4">Issue Details</h3>

							<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
								<!-- Department -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Department</label
									>
									<select
										v-model="department"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">Select department</option>
										<option value="emergency">Emergency</option>
										<option value="surgery">Surgery</option>
										<option value="icu">ICU</option>
										<option value="cardiology">Cardiology</option>
										<option value="oncology">Oncology</option>
										<option value="pediatrics">Pediatrics</option>
									</select>
								</div>

								<!-- Requesting Doctor -->
								<div>
									<label class="block text-sm font-medium text-gray-700 mb-2"
										>Requesting Doctor</label
									>
									<select
										v-model="requestingDoctor"
										class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">Select doctor</option>
										<option value="dr-smith">Dr. Smith</option>
										<option value="dr-johnson">Dr. Johnson</option>
										<option value="dr-williams">Dr. Williams</option>
										<option value="dr-brown">Dr. Brown</option>
									</select>
								</div>
							</div>

							<!-- Issue Date -->
							<div class="mb-6">
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Issue Date</label
								>
								<input
									type="date"
									v-model="issueDate"
									class="w-full md:w-auto px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
								/>
							</div>

							<!-- Emergency Request -->
							<div class="mb-6">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="emergency-request"
											type="checkbox"
											v-model="emergencyRequest"
											class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2"
										/>
									</div>
									<div class="ml-3">
										<label
											for="emergency-request"
											class="text-sm font-medium text-gray-700"
										>
											Emergency Request
										</label>
										<p class="text-xs text-gray-500">
											Mark this if the blood is needed for an emergency
											situation.
										</p>
									</div>
								</div>
							</div>

							<!-- Purpose -->
							<div class="mb-6">
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Purpose</label
								>
								<textarea
									v-model="purpose"
									rows="3"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									placeholder="Describe the purpose of this blood issue"
								></textarea>
							</div>

							<!-- Additional Notes -->
							<div class="mb-6">
								<label class="block text-sm font-medium text-gray-700 mb-2"
									>Additional Notes</label
								>
								<textarea
									v-model="additionalNotes"
									rows="3"
									class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									placeholder="Any additional information or special instructions"
								></textarea>
							</div>
						</div>

						<!-- Form Actions -->
						<div
							class="flex flex-col sm:flex-row justify-end space-y-3 sm:space-y-0 sm:space-x-4 pt-6 border-t border-gray-200"
						>
							<button
								type="button"
								@click="handleCancel"
								class="w-full sm:w-auto px-6 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors"
							>
								Cancel
							</button>
							<button
								type="submit"
								class="w-full sm:w-auto px-6 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gray-900 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 transition-colors"
							>
								Issue Blood
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

// Form data
const recipientType = ref('hospital')
const selectedPatient = ref('')
const bloodType = ref('')
const numberOfUnits = ref(1)
const department = ref('')
const requestingDoctor = ref('')
const issueDate = ref(new Date().toISOString().split('T')[0]) // Today's date
const emergencyRequest = ref(false)
const purpose = ref('')
const additionalNotes = ref('')

// Form handlers
const handleSubmit = () => {
	// Validate required fields
	if (
		!selectedPatient.value ||
		!bloodType.value ||
		!department.value ||
		!requestingDoctor.value
	) {
		alert('Please fill in all required fields')
		return
	}

	// Collect form data
	const formData = {
		recipientType: recipientType.value,
		selectedPatient: selectedPatient.value,
		bloodType: bloodType.value,
		numberOfUnits: numberOfUnits.value,
		department: department.value,
		requestingDoctor: requestingDoctor.value,
		issueDate: issueDate.value,
		emergencyRequest: emergencyRequest.value,
		purpose: purpose.value,
		additionalNotes: additionalNotes.value,
	}

	console.log('Form submitted:', formData)
	alert('Blood issue form submitted successfully!')
}

const handleCancel = () => {
	// Reset form or navigate away
	if (confirm('Are you sure you want to cancel? All unsaved changes will be lost.')) {
		// Reset form data
		recipientType.value = 'hospital'
		selectedPatient.value = ''
		bloodType.value = ''
		numberOfUnits.value = 1
		department.value = ''
		requestingDoctor.value = ''
		issueDate.value = new Date().toISOString().split('T')[0]
		emergencyRequest.value = false
		purpose.value = ''
		additionalNotes.value = ''
	}
}
</script>
