<template>
	<div class="min-h-screen p-4 md:p-6">
		<div class="">
			<!-- Header -->
			<div class="flex items-center justify-between mb-8">
				<div>
					<div class="flex items-center gap-3 mb-2">
						<button
							@click="goBack"
							class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 19l-7-7 7-7"
								></path>
							</svg>
						</button>
						<h1 class="text-2xl md:text-3xl font-bold text-gray-900">
							Add Department
						</h1>
					</div>
					<p class="text-gray-600 ml-11">Create a new department in your clinic</p>
				</div>
				<div class="flex items-center gap-2 text-sm text-gray-500">
					<span>Back to Departments</span>
				</div>
			</div>

			<form @submit.prevent="createDepartment" class="space-y-8">
				<!-- Department Information Section -->
				<div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
					<div class="mb-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-1">
							Department Information
						</h2>
						<p class="text-sm text-gray-600">
							Enter the details for the new department
						</p>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<!-- Department Name -->
						<div>
							<label
								for="departmentName"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Department Name
							</label>
							<input
								id="departmentName"
								v-model="form.departmentName"
								type="text"
								placeholder="e.g. Cardiology"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								required
							/>
							<p class="text-xs text-gray-500 mt-1">
								The official name of the department
							</p>
						</div>

						<!-- Head of Department -->
						<div>
							<label
								for="headOfDepartment"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Head of Department
							</label>
							<select
								id="headOfDepartment"
								v-model="form.headOfDepartment"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								required
							>
								<option value="">Select a doctor</option>
								<option
									v-for="doctor in availableDoctors"
									:key="doctor.id"
									:value="doctor.id"
								>
									{{ doctor.name }}
								</option>
							</select>
							<p class="text-xs text-gray-500 mt-1">
								The doctor who will lead this department
							</p>
						</div>

						<!-- Location -->
						<div>
							<label
								for="location"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Location
							</label>
							<input
								id="location"
								v-model="form.location"
								type="text"
								placeholder="e.g. Building A, Floor 3"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								required
							/>
							<p class="text-xs text-gray-500 mt-1">
								Physical location of the department
							</p>
						</div>

						<!-- Status -->
						<div>
							<label
								for="status"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Status
							</label>
							<select
								id="status"
								v-model="form.status"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="Active">Active</option>
								<option value="Inactive">Inactive</option>
							</select>
							<p class="text-xs text-gray-500 mt-1">Current operational status</p>
						</div>

						<!-- Contact Email -->
						<div>
							<label
								for="contactEmail"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Contact Email
							</label>
							<input
								id="contactEmail"
								v-model="form.contactEmail"
								type="email"
								placeholder="department@clinic.com"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								required
							/>
							<p class="text-xs text-gray-500 mt-1">Department contact email</p>
						</div>

						<!-- Contact Phone -->
						<div>
							<label
								for="contactPhone"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								Contact Phone
							</label>
							<input
								id="contactPhone"
								v-model="form.contactPhone"
								type="tel"
								placeholder="(XXX) XXX-XXXX"
								class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								required
							/>
							<p class="text-xs text-gray-500 mt-1">Department contact phone</p>
						</div>
					</div>

					<!-- Description -->
					<div class="mt-6">
						<label
							for="description"
							class="block text-sm font-medium text-gray-700 mb-2"
						>
							Description
						</label>
						<textarea
							id="description"
							v-model="form.description"
							rows="4"
							placeholder="Provide a description of the department's purpose, specialities, and functions..."
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
						></textarea>
						<p class="text-xs text-gray-500 mt-1">
							Detailed description of the department
						</p>
					</div>
				</div>

				<!-- Assign Staff Section -->
				<div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
					<div class="mb-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-1">Assign Staff</h2>
						<p class="text-sm text-gray-600">
							Add staff members to assign to this department
						</p>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
						<div
							v-for="staffMember in staffMembers"
							:key="staffMember.id"
							class="flex items-start space-x-3"
						>
							<input
								:id="`staff-${staffMember.id}`"
								v-model="form.assignedStaff"
								:value="staffMember.id"
								type="checkbox"
								class="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
							/>
							<div class="flex-1">
								<label
									:for="`staff-${staffMember.id}`"
									class="block text-sm font-medium text-gray-900 cursor-pointer"
								>
									{{ staffMember.name }}
								</label>
								<p class="text-xs text-gray-500">{{ staffMember.role }}</p>
							</div>
						</div>
					</div>
				</div>

				<!-- Available Services Section -->
				<div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
					<div class="mb-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-1">
							Available Services
						</h2>
						<p class="text-sm text-gray-600">
							Select services that will be offered by this department
						</p>
					</div>

					<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
						<div
							v-for="service in availableServices"
							:key="service.id"
							class="flex items-start space-x-3"
						>
							<input
								:id="`service-${service.id}`"
								v-model="form.selectedServices"
								:value="service.id"
								type="checkbox"
								class="mt-1 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
							/>
							<div class="flex-1">
								<label
									:for="`service-${service.id}`"
									class="block text-sm font-medium text-gray-900 cursor-pointer"
								>
									{{ service.name }}
								</label>
								<p class="text-xs text-gray-500">{{ service.description }}</p>
							</div>
						</div>
					</div>
				</div>

				<!-- Form Actions -->
				<div class="flex flex-col sm:flex-row gap-3 sm:justify-end">
					<button
						type="button"
						@click="goBack"
						class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
					>
						Cancel
					</button>
					<button
						type="submit"
						class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors"
					>
						Create Department
					</button>
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

// Form data
const form = ref({
	departmentName: '',
	headOfDepartment: '',
	location: '',
	status: 'Active',
	contactEmail: '',
	contactPhone: '',
	description: '',
	assignedStaff: [],
	selectedServices: [],
})

// Available doctors for head of department
const availableDoctors = ref([
	{ id: 1, name: 'Dr. Sarah Johnson' },
	{ id: 2, name: 'Dr. Michael Chen' },
	{ id: 3, name: 'Dr. Emily Rodriguez' },
	{ id: 4, name: 'Dr. James Wilson' },
	{ id: 5, name: 'Dr. Lisa Thompson' },
	{ id: 6, name: 'Dr. Robert Kim' },
	{ id: 7, name: 'Dr. Jennifer Martinez' },
	{ id: 8, name: 'Dr. David Brown' },
	{ id: 9, name: 'Dr. Susan Lee' },
	{ id: 10, name: 'Dr. Thomas Garcia' },
])

// Staff members available for assignment
const staffMembers = ref([
	{ id: 1, name: 'Dr. Sarah Johnson', role: 'Cardiologist' },
	{ id: 2, name: 'Dr. Michael Chen', role: 'Neurologist' },
	{ id: 3, name: 'Dr. Emily Rodriguez', role: 'Pediatrician' },
	{ id: 4, name: 'Nurse Robert Taylor', role: 'Registered Nurse' },
	{ id: 5, name: 'Nurse Jessica Adams', role: 'Pediatric Nurse' },
	{ id: 6, name: 'Dr. James Wilson', role: 'Orthopedic Surgeon' },
])

// Available services
const availableServices = ref([
	{
		id: 1,
		name: 'General Consultation',
		description: 'Initial patient assessment and diagnosis',
	},
	{
		id: 2,
		name: 'Specialized Treatment',
		description: 'Advanced procedures specific to department',
	},
	{ id: 3, name: 'Diagnostic Testing', description: 'Comprehensive tests and screenings' },
	{ id: 4, name: 'Emergency Care', description: 'Urgent medical attention' },
	{ id: 5, name: 'Follow-up Visits', description: 'Post treatment monitoring and care' },
	{ id: 6, name: 'Preventive Care', description: 'Health maintenance and disease prevention' },
])

// Methods
const goBack = () => {
	// In a real app, this would navigate back to the departments list
	console.log('Navigate back to departments list')
}

const createDepartment = () => {
	// Validate form
	if (!form.value.departmentName || !form.value.headOfDepartment || !form.value.location) {
		alert('Please fill in all required fields')
		return
	}

	// In a real app, this would submit the form data to the backend
	console.log('Creating department with data:', form.value)

	// Show success message and redirect
	alert('Department created successfully!')
	goBack()
}
</script>
