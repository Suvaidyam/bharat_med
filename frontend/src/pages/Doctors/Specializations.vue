<template>
	<div class="min-h-screen bg-white">
		<!-- Header -->
		<div class="bg-white shadow-sm border-b px-4 py-4 md:px-6">
			<div class="flex items-center gap-3">
				<button class="p-2 hover:bg-gray-100 rounded-lg">
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
						/>
					</svg>
				</button>
				<div>
					<h1 class="text-xl font-semibold text-gray-900">Specializations</h1>
					<p class="text-sm text-gray-600">
						Manage medical specializations in your clinic.
					</p>
				</div>
			</div>
		</div>

		<!-- Main Content -->
		<div class="p-4 md:p-6">
			<!-- Section Header -->
			<div class="mb-6">
				<h2 class="text-lg font-semibold text-gray-900 mb-2">Specializations List</h2>
				<p class="text-sm text-gray-600">View and manage all medical specializations.</p>
			</div>

			<!-- Search and Add Button -->
			<div class="flex flex-col sm:flex-row gap-4 mb-6">
				<div class="flex-1 relative">
					<div
						class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
					>
						<svg
							class="w-4 h-4 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
							/>
						</svg>
					</div>
					<input
						v-model="searchQuery"
						type="text"
						placeholder="Search specializations..."
						class="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm"
					/>
				</div>
				<button
					@click="openAddModal"
					class="bg-gray-900 text-white px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2 text-sm font-medium"
				>
					<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 4v16m8-8H4"
						/>
					</svg>
					Add Specialization
				</button>
			</div>

			<!-- Specializations Table -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
				<!-- Table Header -->
				<div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
					<div
						class="grid grid-cols-12 gap-4 text-xs font-medium text-gray-500 uppercase tracking-wider"
					>
						<div class="col-span-12 md:col-span-2">Name</div>
						<div class="col-span-12 md:col-span-3 hidden md:block">Description</div>
						<div class="col-span-12 md:col-span-1 hidden md:block">Doctors</div>
						<div class="col-span-12 md:col-span-2 hidden md:block">Department</div>
						<div class="col-span-12 md:col-span-1 hidden md:block">Status</div>
						<div class="col-span-12 md:col-span-1 hidden md:block">Actions</div>
					</div>
				</div>

				<!-- Table Body -->
				<div class="divide-y divide-gray-200">
					<div
						v-for="specialization in filteredSpecializations"
						:key="specialization.id"
						class="px-6 py-4 hover:bg-gray-50 transition-colors"
					>
						<!-- Desktop View -->
						<div class="hidden md:grid grid-cols-12 gap-4 items-center">
							<div class="col-span-2">
								<div class="font-medium text-gray-900">
									{{ specialization.name }}
								</div>
							</div>
							<div class="col-span-3">
								<div class="text-sm text-gray-600">
									{{ specialization.description }}
								</div>
							</div>
							<div class="col-span-1">
								<div class="text-sm text-gray-900">
									{{ specialization.doctors }}
								</div>
							</div>
							<div class="col-span-2">
								<div class="text-sm text-gray-600">
									{{ specialization.department }}
								</div>
							</div>
							<div class="col-span-1">
								<span
									:class="[
										'inline-flex px-2 py-1 text-xs font-medium rounded-full',
										specialization.status === 'Active'
											? 'bg-green-100 text-green-800'
											: 'bg-yellow-100 text-yellow-800',
									]"
								>
									{{ specialization.status }}
								</span>
							</div>
							<div class="col-span-1">
								<button
									@click="openActionsMenu(specialization.id)"
									class="p-1 hover:bg-gray-100 rounded-lg relative"
								>
									<svg
										class="w-4 h-4 text-gray-400"
										fill="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"
										/>
									</svg>

									<!-- Actions Dropdown -->
									<div
										v-if="activeActionsMenu === specialization.id"
										class="absolute right-0 top-full mt-1 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-1 z-10"
									>
										<button
											@click="editSpecialization(specialization)"
											class="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50"
										>
											Edit
										</button>
										<button
											@click="toggleStatus(specialization)"
											class="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50"
										>
											{{
												specialization.status === 'Active'
													? 'Deactivate'
													: 'Activate'
											}}
										</button>
										<button
											@click="deleteSpecialization(specialization.id)"
											class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50"
										>
											Delete
										</button>
									</div>
								</button>
							</div>
						</div>

						<!-- Mobile View -->
						<div class="md:hidden">
							<div class="flex justify-between items-start mb-2">
								<div>
									<div class="font-medium text-gray-900">
										{{ specialization.name }}
									</div>
									<div class="text-sm text-gray-600 mt-1">
										{{ specialization.department }}
									</div>
								</div>
								<div class="flex items-center gap-2">
									<span
										:class="[
											'inline-flex px-2 py-1 text-xs font-medium rounded-full',
											specialization.status === 'Active'
												? 'bg-green-100 text-green-800'
												: 'bg-yellow-100 text-yellow-800',
										]"
									>
										{{ specialization.status }}
									</span>
									<button
										@click="openActionsMenu(specialization.id)"
										class="p-1 hover:bg-gray-100 rounded-lg relative"
									>
										<svg
											class="w-4 h-4 text-gray-400"
											fill="currentColor"
											viewBox="0 0 24 24"
										>
											<path
												d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"
											/>
										</svg>

										<!-- Mobile Actions Dropdown -->
										<div
											v-if="activeActionsMenu === specialization.id"
											class="absolute right-0 top-full mt-1 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-1 z-10"
										>
											<button
												@click="editSpecialization(specialization)"
												class="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50"
											>
												Edit
											</button>
											<button
												@click="toggleStatus(specialization)"
												class="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50"
											>
												{{
													specialization.status === 'Active'
														? 'Deactivate'
														: 'Activate'
												}}
											</button>
											<button
												@click="deleteSpecialization(specialization.id)"
												class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50"
											>
												Delete
											</button>
										</div>
									</button>
								</div>
							</div>
							<div class="text-sm text-gray-600 mb-2">
								{{ specialization.description }}
							</div>
							<div class="text-sm text-gray-500">
								{{ specialization.doctors }} doctors
							</div>
						</div>
					</div>
				</div>

				<!-- Empty State -->
				<div v-if="filteredSpecializations.length === 0" class="px-6 py-12 text-center">
					<svg
						class="w-12 h-12 text-gray-400 mx-auto mb-4"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
						/>
					</svg>
					<h3 class="text-lg font-medium text-gray-900 mb-2">
						No specializations found
					</h3>
					<p class="text-gray-600 mb-4">
						{{
							searchQuery
								? 'Try adjusting your search terms.'
								: 'Get started by adding your first specialization.'
						}}
					</p>
					<button
						v-if="!searchQuery"
						@click="openAddModal"
						class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
					>
						Add Specialization
					</button>
				</div>
			</div>
		</div>
		<section class="p-6 bg-white rounded shadow mx-7">
			<h2 class="text-2xl font-semibold">Specialization Statistics</h2>
			<p class="text-sm text-gray-500 mb-6">
				Overview of specializations and associated doctors.
			</p>

			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
				<div v-for="item in specialization" :key="item.title" class="p-4 border rounded">
					<h3 class="text-lg font-semibold mb-2">{{ item.title }}</h3>
					<div class="text-2xl font-bold">{{ item.count }}</div>
					<div class="text-sm text-gray-500">Doctors</div>
					<div class="mt-2 w-full h-1 bg-gray-100">
						<div
							class="h-1 bg-black"
							:style="{ width: `${(item.count / maxCount) * 100}%` }"
						></div>
					</div>
				</div>
			</div>
		</section>

		<!-- Add/Edit Modal -->
		<div
			v-if="showModal"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
			@click="closeModal"
		>
			<div @click.stop class="bg-white rounded-lg shadow-xl w-full max-w-md p-6">
				<h3 class="text-lg font-semibold text-gray-900 mb-4">
					{{ editingSpecialization ? 'Edit Specialization' : 'Add New Specialization' }}
				</h3>

				<form @submit.prevent="saveSpecialization" class="space-y-4">
					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
						<input
							v-model="formData.name"
							type="text"
							required
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							placeholder="Enter specialization name"
						/>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1"
							>Description</label
						>
						<textarea
							v-model="formData.description"
							required
							rows="3"
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							placeholder="Enter description"
						></textarea>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1"
							>Department</label
						>
						<select
							v-model="formData.department"
							required
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						>
							<option value="">Select department</option>
							<option v-for="dept in departments" :key="dept" :value="dept">
								{{ dept }}
							</option>
						</select>
					</div>

					<div class="flex justify-end gap-3 pt-4">
						<button
							type="button"
							@click="closeModal"
							class="px-4 py-2 text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
						>
							Cancel
						</button>
						<button
							type="submit"
							class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
						>
							{{ editingSpecialization ? 'Update' : 'Add' }}
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// Reactive data
const searchQuery = ref('')
const showModal = ref(false)
const editingSpecialization = ref(null)
const activeActionsMenu = ref(null)
const specialization = [
	{ title: 'Cardiology', count: 5 },
	{ title: 'Neurology', count: 3 },
	{ title: 'Pediatrics', count: 7 },
	{ title: 'Orthopedics', count: 4 },
]

// Form data
const formData = ref({
	name: '',
	description: '',
	department: '',
})

// Sample data
const specializations = ref([
	{
		id: 1,
		name: 'Cardiology',
		description: 'Diagnosis and treatment of heart disorders',
		doctors: 5,
		department: 'Internal Medicine',
		status: 'Active',
	},
	{
		id: 2,
		name: 'Neurology',
		description: 'Diagnosis and treatment of disorders of the nervous system',
		doctors: 3,
		department: 'Neuroscience',
		status: 'Active',
	},
	{
		id: 3,
		name: 'Pediatrics',
		description: 'Medical care of infants, children, and adolescents',
		doctors: 7,
		department: 'Child Health',
		status: 'Active',
	},
	{
		id: 4,
		name: 'Orthopedics',
		description: 'Treatment of the musculoskeletal system',
		doctors: 4,
		department: 'Surgery',
		status: 'Active',
	},
	{
		id: 5,
		name: 'Dermatology',
		description: 'Diagnosis and treatment of skin disorders',
		doctors: 2,
		department: 'Skin Health',
		status: 'Active',
	},
	{
		id: 6,
		name: 'Psychiatry',
		description: 'Diagnosis, prevention, and treatment of mental disorders',
		doctors: 3,
		department: 'Mental Health',
		status: 'Inactive',
	},
	{
		id: 7,
		name: 'Ophthalmology',
		description: 'Diagnosis and treatment of eye disorders',
		doctors: 2,
		department: 'Eye Care',
		status: 'Active',
	},
	{
		id: 8,
		name: 'Gynecology',
		description: 'Health of the female reproductive system',
		doctors: 4,
		department: "Women's Health",
		status: 'Active',
	},
])

const departments = ref([
	'Internal Medicine',
	'Neuroscience',
	'Child Health',
	'Surgery',
	'Skin Health',
	'Mental Health',
	'Eye Care',
	"Women's Health",
])

// Computed properties
const filteredSpecializations = computed(() => {
	if (!searchQuery.value) return specializations.value

	return specializations.value.filter(
		(spec) =>
			spec.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			spec.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			spec.department.toLowerCase().includes(searchQuery.value.toLowerCase()),
	)
})

// Methods
const openAddModal = () => {
	editingSpecialization.value = null
	formData.value = {
		name: '',
		description: '',
		department: '',
	}
	showModal.value = true
}

const editSpecialization = (specialization) => {
	editingSpecialization.value = specialization
	formData.value = {
		name: specialization.name,
		description: specialization.description,
		department: specialization.department,
	}
	showModal.value = true
	activeActionsMenu.value = null
}

const closeModal = () => {
	showModal.value = false
	editingSpecialization.value = null
	formData.value = {
		name: '',
		description: '',
		department: '',
	}
}

const saveSpecialization = () => {
	if (editingSpecialization.value) {
		// Update existing specialization
		const index = specializations.value.findIndex(
			(s) => s.id === editingSpecialization.value.id,
		)
		if (index !== -1) {
			specializations.value[index] = {
				...specializations.value[index],
				...formData.value,
			}
		}
	} else {
		// Add new specialization
		const newId = Math.max(...specializations.value.map((s) => s.id)) + 1
		specializations.value.push({
			id: newId,
			...formData.value,
			doctors: 0,
			status: 'Active',
		})
	}

	closeModal()
}

const openActionsMenu = (id) => {
	activeActionsMenu.value = activeActionsMenu.value === id ? null : id
}

const toggleStatus = (specialization) => {
	const index = specializations.value.findIndex((s) => s.id === specialization.id)
	if (index !== -1) {
		specializations.value[index].status =
			specializations.value[index].status === 'Active' ? 'Inactive' : 'Active'
	}
	activeActionsMenu.value = null
}

const deleteSpecialization = (id) => {
	if (confirm('Are you sure you want to delete this specialization?')) {
		const index = specializations.value.findIndex((s) => s.id === id)
		if (index !== -1) {
			specializations.value.splice(index, 1)
		}
	}
	activeActionsMenu.value = null
}

const handleClickOutside = (event) => {
	if (!event.target.closest('.relative')) {
		activeActionsMenu.value = null
	}
}

// Lifecycle
onMounted(() => {
	document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
	document.removeEventListener('click', handleClickOutside)
})
</script>
